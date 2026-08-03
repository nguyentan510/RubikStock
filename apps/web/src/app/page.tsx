import { publicEnv } from "../lib/env"

const foundationItems = [
  {
    label: "API",
    value: "FastAPI",
    note: "Health, readiness, metadata, OpenAPI, and request logging foundation.",
  },
  {
    label: "Web",
    value: "Next.js PWA",
    note: "Typed UI shell with a clear path for warehouse and B2B workflows.",
  },
  {
    label: "Data",
    value: "Supabase + PostgreSQL",
    note: "Local Postgres for dev, remote Supabase for staging and production.",
  },
  {
    label: "Ops",
    value: "GitHub Actions",
    note: "Docs validation, API tests, web build, and secret scanning.",
  },
]

const nextSteps = [
  "Chốt license repository và cấu hình remote GitHub.",
  "Bổ sung domain models và migrations đầu tiên sau khi D2 foundation ổn định.",
  "Kết nối local Postgres, API readyz, và web env khi triển khai dev flow.",
]

const docLinks = [
  {
    href: "/docs",
    title: "Documentation map",
    description: "Bản đồ tài liệu và thứ tự đọc chính thức của RubikStock.",
  },
  {
    href: "https://github.com",
    title: "GitHub deployment pipeline",
    description: "CI, secrets, environments, và luồng release được thiết kế cho public source.",
  },
]

export default function HomePage() {
  return (
    <main>
      <div className="shell">
        <section className="hero">
          <span className="eyebrow">D2 Technical foundation</span>
          <h1 className="title">RubikStock đang dựng nền kỹ thuật cho vận hành kho B2B.</h1>
          <p className="lede">
            Đây là xương sống ban đầu cho FastAPI API, Next.js web shell, PostgreSQL local,
            Supabase-ready configuration, migration scaffold, logging, OpenAPI, và CI.
          </p>
        </section>

        <section className="status-grid" aria-label="Foundation summary">
          {foundationItems.map((item) => (
            <article className="card" key={item.label}>
              <span className="metric">{item.label}</span>
              <strong>{item.value}</strong>
              <p>{item.note}</p>
            </article>
          ))}
        </section>

        <section className="cards">
          <article className="card wide">
            <h2>Current slice</h2>
            <p>
              D2 tập trung vào setup có thể lặp lại, smoke endpoint, migration scaffold, and
              CI gates. Business logic vẫn chưa được đưa vào code.
            </p>
            <p>
              Public env hiện tại: <strong>{publicEnv.appName}</strong> /{" "}
              <strong>{publicEnv.apiBaseUrl}</strong>
            </p>
          </article>

          <article className="card">
            <h3>Next steps</h3>
            <ul className="list">
              {nextSteps.map((step) => (
                <li key={step}>{step}</li>
              ))}
            </ul>
          </article>

          <article className="card">
            <h3>Entry points</h3>
            <div className="link-grid">
              {docLinks.map((link) => (
                <a className="link-card" href={link.href} key={link.title}>
                  <strong>{link.title}</strong>
                  <span>{link.description}</span>
                </a>
              ))}
            </div>
          </article>
        </section>
      </div>
    </main>
  )
}
