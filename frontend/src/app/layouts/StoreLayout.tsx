import { Activity, ShoppingCart } from "lucide-react";
import { Link, NavLink, Outlet } from "react-router-dom";
export default function StoreLayout() {
  return <div className="store-shell"><header className="store-header"><Link to="/store" className="brand"><span className="brand-mark">B</span><span>BOSCH<small>DEMO COMMERCE</small></span></Link><nav><NavLink to="/store">Home</NavLink><NavLink to="/store/products">Products</NavLink><NavLink to="/store/cart"><ShoppingCart size={16}/> Cart</NavLink><NavLink to="/observability"><Activity size={16}/> Monitoring</NavLink></nav></header><Outlet/><footer className="store-footer">Bosch demo storefront · Synthetic catalogue · No real purchases are processed</footer></div>;
}
