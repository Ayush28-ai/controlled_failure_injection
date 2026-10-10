import { FlaskConical, Gauge, History, ShieldCheck, ShoppingBag } from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";
export default function ExperimentLayout() {
  return <div className="shell"><aside className="sidebar">
    <a className="brand" href="/observability"><span className="brand-mark">B</span><span>BOSCH<small>RESILIENCE LAB</small></span></a>
    <div className="nav-label">EXPERIMENT LAB</div><nav>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments"><Gauge size={17}/>Experiment home</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments/scenarios"><FlaskConical size={17}/>Scenarios</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments/run"><ShieldCheck size={17}/>Run simulation</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments/impact"><Gauge size={17}/>Impact review</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/experiments/recovery"><History size={17}/>Recovery</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/observability"><Gauge size={17}/>Observability</NavLink>
      <NavLink className={({isActive})=>`nav-link ${isActive?"active":""}`} to="/store"><ShoppingBag size={17}/>Demo store</NavLink>
    </nav><div className="sidebar-bottom"><span className="status-dot"/>Simulation only — no real faults</div>
  </aside><div className="main-column"><header className="topbar"><div><span className="eyebrow">EXPERIMENT WORKSPACE</span><span className="topbar-title">Controlled failure simulation</span></div><span className="pill"><ShieldCheck size={14}/> GUARDED</span></header><Outlet/></div></div>;
}
