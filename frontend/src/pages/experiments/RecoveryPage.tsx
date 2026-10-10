import { useState } from "react";
import PageHeader from "../../components/PageHeader";
import { recoverExperiment } from "../../api/experiments";
export default function RecoveryPage(){
 const [id,setId]=useState("");const [busy,setBusy]=useState(false);const [result,setResult]=useState<any>(null);const [error,setError]=useState("");
 async function submit(e:React.FormEvent){e.preventDefault();setBusy(true);setError("");setResult(null);try{setResult(await recoverExperiment(Number(id)))}catch(e){setError(e instanceof Error?e.message:"Recovery request failed")}finally{setBusy(false)}}
 return <main className="page"><PageHeader eyebrow="SAFETY & RECOVERY" title="Recovery record" description="The current backend intentionally performs no real rollback because the experiment runner is simulation-only."/><section className="panel form-panel"><form onSubmit={submit}><label className="field-label" htmlFor="experiment-id">Experiment ID</label><input id="experiment-id" className="input" type="number" min="1" required value={id} onChange={e=>setId(e.target.value)} placeholder="e.g. 1"/><button className="button" disabled={busy}>{busy?"Checking…":"Check recovery status"}</button></form>{error&&<p className="form-error">{error}</p>}{result&&<><h3>Recovery response</h3><pre className="json-view">{JSON.stringify(result,null,2)}</pre></>}</section><div className="notice"><strong>Safety note</strong><p>Do not interpret “not required” as proof that a production system recovered. No production changes are made by this implementation.</p></div></main>
}
