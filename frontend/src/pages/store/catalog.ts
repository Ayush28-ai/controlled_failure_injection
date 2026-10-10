export type Product = { id: string; name: string; category: string; price: number; description: string; accent: string };
export const products: Product[] = [
 {id:"sensor-kit",name:"Connected Sensor Kit",category:"Sensors",price:89,description:"A demo kit representing connected industrial sensing.",accent:"sensor"},
 {id:"edge-gateway",name:"Industrial Edge Gateway",category:"Connectivity",price:149,description:"A synthetic catalogue item for edge connectivity workflows.",accent:"gateway"},
 {id:"smart-relay",name:"Smart Control Relay",category:"Controls",price:42,description:"A demo control component for the storefront flow.",accent:"relay"},
 {id:"monitor-display",name:"Monitoring Display",category:"Monitoring",price:219,description:"A demo display product for catalogue and cart testing.",accent:"display"}
];
export type CartLine = { productId: string; quantity: number };
export const CART_KEY = "bosch-demo-cart";
export function readCart(): CartLine[] { try { const raw=localStorage.getItem(CART_KEY); return raw?JSON.parse(raw):[]; } catch { return []; } }
export function writeCart(cart: CartLine[]) { localStorage.setItem(CART_KEY,JSON.stringify(cart)); }
