import { useEffect, useState } from "react";
import PageHeader from "../../components/PageHeader";
import { ErrorState, Loading } from "../../components/States";
import { getHealth, getTopology } from "../../api/metrics";
export default function ServiceHealthPage(){
 const [data,setData]=useState<any>(null);const [error,setError]=useState("");
 async function load(){try{setError("");const [health,topology]=await Promise.all([getHealth(),getTopology()]);setData({health,topology});}catch(e){setError(e instanceof Error?e.message:"Could not load service data");}}
 useEffect(()=>{void load()},[]);
 return <main className="page"><PageHeader eyebrow="OBSERVABILITY" title="Service health" description="Service inventory and backend reachability. A healthy API does not imply every downstream service has an active probe." actions={<button className="button secondary" onClick={load}>Refresh</button>}/>{error&&<ErrorState message={error} onRetry={load}/ >}{!data&&!error&&<Loading/>}{data&&<><div className="notice"><strong>Health check:</strong> {data.health.status} · last checked {new Date(data.health.timestamp).toLocaleString()}</div><div className="service-grid">{data.topology.services.map((s:any)=><article className="service-card" key={s.id}><div className="service-card-top"><span className="service-symbol">{s.type==="database"?"DB":s.type==="frontend"?"UI":s.type==="dependency"?"DEP":"API"}</span><span className="tag neutral">Configured</span></div><h3>{s.name}</h3><p>{s.id}</p><small>Type: {s.type}</small></article>)}</div><section className="panel"><h2>Dependency map</h2>{data.topology.dependencies.map((d:any)=><div className="dependency-row" key={d.source+d.target}><code>{d.source}</code><span>→</span><code>{d.target}</code></div>)}</section></>}</main>;
}
