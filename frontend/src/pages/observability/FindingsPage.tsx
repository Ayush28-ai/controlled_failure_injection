import { useEffect, useState } from "react";
import PageHeader from "../../components/PageHeader";
import { ErrorState, Loading, EmptyState } from "../../components/States";
import { listFindings, type Finding } from "../../api/findings";
export default function FindingsPage(){
 const [items,setItems]=useState<Finding[]>([]);const [error,setError]=useState("");const [loading,setLoading]=useState(true);
 async function load(){setLoading(true);setError("");try{setItems(await listFindings())}catch(e){setError(e instanceof Error?e.message:"Could not load findings")}finally{setLoading(false)}}
 useEffect(()=>{void load()},[]);
 return <main className="page"><PageHeader eyebrow="OBSERVABILITY" title="Findings" description="Evidence and recommendations saved by experiment analysis." actions={<button className="button secondary" onClick={load}>Refresh</button>}/>{error&&<ErrorState message={error} onRetry={load}/ >}{loading?<Loading/>:items.length===0?<EmptyState title="No findings yet" detail="Run a simulation and add validated observations when evidence is available."/>:<div className="finding-list">{items.map(f=><article className="panel finding" key={f.id}><div className="finding-top"><span className={`severity severity-${f.severity}`}>{f.severity}</span><span className="muted">Finding #{f.id} · {new Date(f.created_at).toLocaleString()}</span></div><h2>{f.title}</h2>{f.experiment_id&&<p className="muted">Experiment #{f.experiment_id}</p>}<h3>Evidence</h3><p>{f.evidence||"No evidence supplied."}</p><h3>Recommendation</h3><p>{f.recommendation||"No recommendation supplied."}</p></article>)}</div>}</main>;
}
