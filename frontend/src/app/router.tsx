import { Navigate, Route, Routes } from "react-router-dom";
import DashboardLayout from "./layouts/DashboardLayout";
import StoreLayout from "./layouts/StoreLayout";
import ExperimentLayout from "./layouts/ExperimentLayout";
import OverviewPage from "../pages/observability/OverviewPage";
import ServiceHealthPage from "../pages/observability/ServiceHealthPage";
import MetricsPage from "../pages/observability/MetricsPage";
import FindingsPage from "../pages/observability/FindingsPage";
import ExperimentsHistoryPage from "../pages/observability/ExperimentsHistoryPage";
import ExperimentHomePage from "../pages/experiments/ExperimentHomePage";
import ScenarioSelectionPage from "../pages/experiments/ScenarioSelectionPage";
import ExperimentRunPage from "../pages/experiments/ExperimentRunPage";
import LiveImpactPage from "../pages/experiments/LiveImpactPage";
import RecoveryPage from "../pages/experiments/RecoveryPage";
import HomePage from "../pages/store/HomePage";
import ProductsPage from "../pages/store/ProductsPage";
import ProductDetailsPage from "../pages/store/ProductDetailsPage";
import CartPage from "../pages/store/CartPage";
import CheckoutPage from "../pages/store/CheckoutPage";

export default function App() {
  return <Routes>
    <Route path="/" element={<Navigate to="/observability" replace />} />
    <Route element={<DashboardLayout />}>
      <Route path="/observability" element={<OverviewPage />} />
      <Route path="/observability/services" element={<ServiceHealthPage />} />
      <Route path="/observability/metrics" element={<MetricsPage />} />
      <Route path="/observability/findings" element={<FindingsPage />} />
      <Route path="/observability/history" element={<ExperimentsHistoryPage />} />
    </Route>
    <Route element={<ExperimentLayout />}>
      <Route path="/experiments" element={<ExperimentHomePage />} />
      <Route path="/experiments/scenarios" element={<ScenarioSelectionPage />} />
      <Route path="/experiments/run" element={<ExperimentRunPage />} />
      <Route path="/experiments/impact" element={<LiveImpactPage />} />
      <Route path="/experiments/recovery" element={<RecoveryPage />} />
    </Route>
    <Route element={<StoreLayout />}>
      <Route path="/store" element={<HomePage />} />
      <Route path="/store/products" element={<ProductsPage />} />
      <Route path="/store/products/:productId" element={<ProductDetailsPage />} />
      <Route path="/store/cart" element={<CartPage />} />
      <Route path="/store/checkout" element={<CheckoutPage />} />
    </Route>
    <Route path="*" element={<main className="page"><h1>Page not found</h1><a href="/observability">Return to dashboard</a></main>} />
  </Routes>;
}
