"""Validate the RubikStock documentation foundation using only stdlib."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/GOVERNANCE.md",
    "docs/00-product/VISION_AND_SCOPE.md",
    "docs/00-product/GLOSSARY.md",
    "docs/00-product/OPEN_QUESTIONS.md",
    "docs/01-business/AS_IS_PROCESS.md",
    "docs/01-business/TO_BE_PROCESS.md",
    "docs/01-business/BUSINESS_RULES.md",
    "docs/01-business/STATE_MACHINES.md",
    "docs/01-business/EXCEPTION_MATRIX.md",
    "docs/01-business/APPROVAL_MATRIX.md",
    "docs/02-architecture/SYSTEM_CONTEXT.md",
    "docs/02-architecture/MODULE_BOUNDARIES.md",
    "docs/02-architecture/DEPLOYMENT_ARCHITECTURE.md",
    "docs/02-architecture/MISA_INTEGRATION_DISCOVERY.md",
    "docs/02-architecture/SECURITY_MODEL.md",
    "docs/02-architecture/REFERENCES.md",
    "docs/02-architecture/adr/0005-local-docker-vps-target.md",
    "docs/03-data/DATA_MODEL.md",
    "docs/03-data/INVENTORY_LEDGER.md",
    "docs/03-data/UOM_CONVERSION.md",
    "docs/03-data/LOT_TRACEABILITY.md",
    "docs/03-data/EXCEL_MIGRATION.md",
    "docs/03-data/SHELF_LIFE_POLICY.md",
    "docs/03-data/templates/README.md",
    "docs/03-data/templates/product_master.csv",
    "docs/03-data/templates/uom_conversion.csv",
    "docs/03-data/templates/customer_shelf_life_policy.csv",
    "docs/03-data/templates/opening_stock.csv",
    "docs/03-data/templates/receipt_capture.csv",
    "docs/03-data/templates/sales_capture.csv",
    "docs/06-delivery/ROADMAP.md",
    "docs/06-delivery/BUILD_ORDER.md",
    "docs/06-delivery/big-plan/README.md",
    "docs/06-delivery/big-plan/MASTER_PLAN.md",
    "docs/06-delivery/big-plan/CURRENT_PHASE_TRACKER.md",
    "docs/06-delivery/big-plan/D0_DECISION_WORKSHOP.md",
    "docs/06-delivery/big-plan/D0_PRODUCT_ACCEPTANCE.md",
    "docs/06-delivery/big-plan/D0_PRODUCT_TRUTH.md",
    "docs/06-delivery/big-plan/D1_BUSINESS_CONTRACTS.md",
    "docs/06-delivery/big-plan/D2_TECHNICAL_FOUNDATION.md",
    "docs/06-delivery/big-plan/M1_MASTER_DATA_WAREHOUSE_MAP.md",
    "docs/06-delivery/big-plan/M2_INVENTORY_LEDGER.md",
    "docs/06-delivery/big-plan/M3_INBOUND.md",
    "docs/06-delivery/big-plan/M4_B2B_OUTBOUND.md",
    "docs/06-delivery/big-plan/M5_QUALITY_EXCEPTIONS.md",
    "docs/06-delivery/big-plan/M6_COMPANY_DELIVERY.md",
    "docs/06-delivery/big-plan/M7_REPLENISHMENT.md",
    "docs/06-delivery/big-plan/M8_PRODUCTION_QUALIFICATION.md",
    "docs/06-delivery/big-plan/M9_OPTIMIZATION.md",
    "docs/06-delivery/IMPLEMENTATION_STATUS.md",
    "docs/06-delivery/TRACEABILITY_MATRIX.md",
    "docs/06-delivery/ACCEPTANCE_GATES.md",
    "docs/07-testing/TEST_STRATEGY.md",
    "docs/07-testing/BUSINESS_SCENARIOS.md",
    "docs/08-operations/ENVIRONMENTS.md",
    "docs/08-operations/DEPLOYMENT_RUNBOOK.md",
    "docs/08-operations/BACKUP_RESTORE.md",
    "docs/08-operations/SECRET_MANAGEMENT.md",
    "docs/08-operations/INCIDENT_RUNBOOK.md",
    "docs/08-operations/MONITORING.md",
    "docs/08-operations/RETENTION_POLICY.md",
)

LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
RULE_ID_RE = re.compile(r"\b(?:INV|LOT|UOM|OUT|QLT|RET|DST|DEL|PLN|AUD|SEC)-\d{3}\b")
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?im)^[ \t]*(?:DATABASE_URL|SUPABASE_SECRET_KEY|SERVICE_ROLE_KEY|JWT_SECRET)"
    r"[ \t]*=[ \t]*([^ \t\r\n#]+)"
)
BIG_PLAN_ROADMAPS = (
    "docs/06-delivery/big-plan/D0_PRODUCT_TRUTH.md",
    "docs/06-delivery/big-plan/D1_BUSINESS_CONTRACTS.md",
    "docs/06-delivery/big-plan/D2_TECHNICAL_FOUNDATION.md",
    "docs/06-delivery/big-plan/M1_MASTER_DATA_WAREHOUSE_MAP.md",
    "docs/06-delivery/big-plan/M2_INVENTORY_LEDGER.md",
    "docs/06-delivery/big-plan/M3_INBOUND.md",
    "docs/06-delivery/big-plan/M4_B2B_OUTBOUND.md",
    "docs/06-delivery/big-plan/M5_QUALITY_EXCEPTIONS.md",
    "docs/06-delivery/big-plan/M6_COMPANY_DELIVERY.md",
    "docs/06-delivery/big-plan/M7_REPLENISHMENT.md",
    "docs/06-delivery/big-plan/M8_PRODUCTION_QUALIFICATION.md",
    "docs/06-delivery/big-plan/M9_OPTIMIZATION.md",
)


def markdown_files() -> list[Path]:
    excluded = {"node_modules", ".venv", ".next", "dist", "build"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and not any(part in excluded for part in path.parts)
    )


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def validate_links(errors: list[str]) -> None:
    for document in markdown_files():
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (document.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors.append(
                    f"broken link: {document.relative_to(ROOT)} -> {raw_target}"
                )


def validate_rule_ids(errors: list[str]) -> None:
    rules_file = ROOT / "docs/01-business/BUSINESS_RULES.md"
    if not rules_file.exists():
        return
    ids = RULE_ID_RE.findall(rules_file.read_text(encoding="utf-8"))
    duplicates = sorted({rule_id for rule_id in ids if ids.count(rule_id) > 1})
    if duplicates:
        errors.append(f"duplicate business rule IDs: {', '.join(duplicates)}")
    if len(ids) < 30:
        errors.append(f"unexpectedly small rule catalog: {len(ids)} rule IDs")


def validate_big_plan_structure(errors: list[str]) -> None:
    required_fragments = (
        "- Status:",
        "- Depends on:",
        "## Outcome",
        "## Work packages",
        "| ID |",
    )
    for relative in BIG_PLAN_ROADMAPS:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                errors.append(f"incomplete big-plan roadmap: {relative} missing {fragment}")
        if "## Exit gate" not in text and "## Exit condition" not in text:
            errors.append(f"incomplete big-plan roadmap: {relative} missing exit criteria")


def validate_clean_start_templates(errors: list[str]) -> None:
    templates = {
        "docs/03-data/templates/product_master.csv": {"sku", "tracking_policy", "base_uom"},
        "docs/03-data/templates/uom_conversion.csv": {
            "sku",
            "base_uom",
            "base_quantity_per_input_uom",
        },
        "docs/03-data/templates/customer_shelf_life_policy.csv": {
            "policy_code",
            "minimum_remaining_days",
            "minimum_remaining_percent",
        },
        "docs/03-data/templates/opening_stock.csv": {
            "count_batch_ref",
            "location_code",
            "inventory_status",
        },
        "docs/03-data/templates/receipt_capture.csv": {
            "receipt_ref",
            "supplier_lot",
            "initial_status",
        },
        "docs/03-data/templates/sales_capture.csv": {
            "order_ref",
            "stockout_flag",
            "lost_sale_quantity",
        },
    }
    for relative, required_headers in templates.items():
        path = ROOT / relative
        if not path.exists():
            continue
        first_line = path.read_text(encoding="utf-8").splitlines()[0]
        headers = {header.strip() for header in first_line.split(",")}
        missing = sorted(required_headers - headers)
        if missing:
            errors.append(f"invalid clean-start template: {relative} missing {', '.join(missing)}")


def validate_d0_decision_register(errors: list[str]) -> None:
    register = ROOT / "docs/00-product/OPEN_QUESTIONS.md"
    if not register.exists():
        return

    decisions: dict[str, str] = {}
    for line in register.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\| (TBD-\d{3}) \|.*\| ([^|]+) \|$", line)
        if match:
            decisions[match.group(1)] = match.group(2).strip()

    expected = {f"TBD-{number:03d}" for number in range(1, 15)}
    missing = sorted(expected - decisions.keys())
    unexpected = sorted(decisions.keys() - expected)
    if missing:
        errors.append(f"D0 decision register missing: {', '.join(missing)}")
    if unexpected:
        errors.append(f"D0 decision register has unexpected IDs: {', '.join(unexpected)}")

    unresolved = sorted(
        decision_id
        for decision_id, status in decisions.items()
        if not status.startswith(("Accepted ", "Deferred ", "Rejected "))
    )
    if unresolved:
        errors.append(f"D0 decisions without disposition: {', '.join(unresolved)}")


def validate_no_committed_secret_values(errors: list[str]) -> None:
    candidates = markdown_files() + [ROOT / ".env.example"]
    for path in candidates:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in SECRET_ASSIGNMENT_RE.finditer(text):
            value = match.group(1).strip().strip('"\'')
            if value and value not in {"<redacted>", "<example>"}:
                errors.append(f"possible committed secret value: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_links(errors)
    validate_rule_ids(errors)
    validate_big_plan_structure(errors)
    validate_clean_start_templates(errors)
    validate_d0_decision_register(errors)
    validate_no_committed_secret_values(errors)

    if errors:
        print("RUBIKSTOCK_DOCS_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(markdown_files())} Markdown files.")
    print("RUBIKSTOCK_DOCS_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
