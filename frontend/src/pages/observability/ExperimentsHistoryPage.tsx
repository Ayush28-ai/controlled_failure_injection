import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import PageHeader from "../../components/PageHeader";
import { ErrorState, Loading, EmptyState } from "../../components/States";
import { listExperiments, type Experiment } from "../../api/experiments";
export default function ExperimentsHistoryPage(){
 const [items,setItems]=useState<Experiment[]>([]);const [error,setError]=useState("");const [loading,setLoading]=useState(true);
 async function load(){setLoading(true);setError("");try{setItems(await listExperiments())}catch(e){setError(e instanceof Error?e.message:"Could not load experiments")}finally{setLoading(false)}}
 useEffect(()=>{void load()},[]);
 return <main className="page"><PageHeader eyebrow="OBSERVABILITY" title="Experiment history" description="Recorded runs and their simulation outcomes." actions={<><Link className="button" to="/experiments/scenarios">New simulation</Link><button className="button secondary" onClick={load}>Refresh</button></>}/>{error&&<ErrorState message={error} onRetry={load}/ >}{loading?<Loading/>:items.length===0?<EmptyState title="No experiments recorded" detail="Create a simulation from the experiment workspace to see it here."/>:<section className="panel"><div className="table-wrap"><table><thead><tr><th>ID</th><th>Scenario</th><th>Target</th><th>Duration</th><th>Mode</th><th>Status</th><th>Created</th></tr></thead><tbody>{items.map(x=><tr key={x.id}><td>#{x.id}</td><td>{x.scenario}</td><td>{x.target_service}</td><td>{x.duration_seconds}s</td><td><span className="tag">Simulation</span></td><td>{x.status}</td><td>{new Date(x.created_at).toLocaleString()}</td></tr>)}</tbody></table></div></section>}</main>;
}
