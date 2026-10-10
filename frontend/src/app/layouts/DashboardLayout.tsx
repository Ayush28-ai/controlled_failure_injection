import { Activity, AlertTriangle, BarChart3, Clock3, Gauge, Network, ShoppingBag, FlaskConical } from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";

const links = [
  { to: "/observability", label: "Overview", icon: Gauge, end: true },
  { to: "/observability/services", label: "Service health", icon: Network },
  { to: "/observability/metrics", label: "Metrics", icon: BarChart3 },
  { to: "/observability/findings", label: "Findings", icon: AlertTriangle },
  { to: "/observability/history", label: "Experiment history", icon: Clock3 },
];
export default function DashboardLayout() {
  return <div className="shell">
    <aside className="sidebar">
      <a className="brand" href="/observability"><span className="brand-mark">B</span><span>BOSCH<small>RESILIENCE LAB</small></span></a>
      <div className="nav-label">MONITORING</div>
      <nav>{links.map(({to,label,icon:Icon,...rest}) => <NavLink key={to} to={to} end={"end" in rest ? rest.end : false} className={({isActive})=>`nav-link ${isActive?"active":""}`}><Icon size={17}/>{label}</NavLink>)}</nav>
      <div className="nav-label">WORKSPACE</div>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments"><FlaskConical size={17}/>Experiments</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/store"><ShoppingBag size={17}/>Demo store</NavLink>
      <div className="sidebar-bottom"><span className="status-dot"/>Simulation mode enabled</div>
    </aside>
    <div className="main-column"><header className="topbar"><div><span className="eyebrow">BOSCH PLATFORM</span><span className="topbar-title">Resilience & Observability</span></div><span className="pill"><Activity size={14}/> CONTROLLED ENVIRONMENT</span></header><Outlet /></div>
  </div>;
}
