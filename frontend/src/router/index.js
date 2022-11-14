import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "../views/home/HomePage";
import LoginPage from "../views/auth/LoginPage";
import RegisterPage from "../views/auth/RegisterPage";
import ForgotPasswordPage from "../views/forgot-password/ForgotPasswordPage";
import ProductPage from "../views/products/ProductPage";
import ProductDetailPage from "../views/products/ProductDetailPage";
import AccountPage from "../views/user/AccountPage";
import TransactionDetailPage from "../views/products/TransactionDetailPage";
import Category from "../views/category";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/product",
    name: "product",
    component: ProductPage,
  },
  {
    path: "/product/:productName",
    name: "productDetail",
    component: ProductDetailPage,
  },
  {
    path: "/transaction/:transactionId",
    name: "transactionDetail",
    component: TransactionDetailPage,
  },

  // ******************************
  // Category
  {
    path: "/product/category/:categoryName",
    name: "category",
    component: Category,
  },
  // ******************************
  {
    path: "/user/account",
    name: "user-account",
    component: AccountPage,
  },
  {
    path: "/login",
    name: "login",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterPage,
  },
  {
    path: "/forgot-password",
    name: "forgotPassword",
    component: ForgotPasswordPage,
  },
  { path: "*", redirect: "/" },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

// chuyển đến trang login nếu chưa được login
// router.beforeEach((to, from, next) => {
//   const publicPages = ["/login", "/register"];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem("user");

//   if (authRequired && !loggedIn) {
//     return next("/login");
//   }

//   next();
// });

export default router;
