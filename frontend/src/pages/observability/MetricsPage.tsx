import { useEffect, useState } from "react";
import PageHeader from "../../components/PageHeader";
import { ErrorState, Loading } from "../../components/States";
import { getMetric, listMetricNames } from "../../api/metrics";
export default function MetricsPage(){
 const [names,setNames]=useState<string[]>([]);const [selected,setSelected]=useState("");const [result,setResult]=useState<any>(null);const [error,setError]=useState("");const [busy,setBusy]=useState(false);
 async function loadNames(){try{setError("");const d=await listMetricNames();setNames(d.available_metrics);if(d.available_metrics.length)setSelected(v=>v||d.available_metrics[0]);}catch(e){setError(e instanceof Error?e.message:"Could not list metrics");}}
 async function loadMetric(name=selected){if(!name)return;setBusy(true);setError("");try{setResult(await getMetric(name));}catch(e){setError(e instanceof Error?e.message:"Could not query metric");}finally{setBusy(false);}}
 useEffect(()=>{void loadNames()},[]);useEffect(()=>{if(selected)void loadMetric(selected)},[selected]);
 return <main className="page"><PageHeader eyebrow="OBSERVABILITY" title="Prometheus metrics" description="Query only the backend's approved metric names. Missing Prometheus data is shown as unavailable, not as zero." actions={<button className="button secondary" onClick={()=>void loadMetric()}>Refresh metric</button>}/>{error&&<ErrorState message={error} onRetry={()=>selected?loadMetric():loadNames()}/ >}{names.length===0&&!error&&<Loading label="Loading metric catalogue…"/>}<section className="panel"><label className="field-label" htmlFor="metric">Approved metric</label><select id="metric" className="input" value={selected} onChange={e=>setSelected(e.target.value)}>{names.map(n=><option key={n} value={n}>{n}</option>)}</select>{busy&&<Loading label="Querying Prometheus…"/>}{result&&<><h3 className="result-title">{result.metric}</h3><pre className="json-view">{JSON.stringify(result.data,null,2)}</pre></>}</section></main>;
}
