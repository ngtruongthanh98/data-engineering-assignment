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
import MenClothes from "../views/category/MenClothes";
import MobileAndGadgets from "../views/category/MobileAndGadgets";
import ConsumerElectronics from "../views/category/ConsumerElectronics";
import ComputerAndAccessories from "../views/category/ComputerAndAccessories";
import Cameras from "../views/category/Cameras";
import Watches from "../views/category/Watches";
import MenShoes from "../views/category/MenShoes";
import HomeAppliances from "../views/category/HomeAppliances";
import SportAndOutdoor from "../views/category/SportAndOutdoor";
import Automotive from "../views/category/Automotive";
import WomenClothes from "../views/category/WomenClothes";
import MomsKidsAndBabies from "../views/category/MomsKidsAndBabies";
import HomeAndLiving from "../views/category/HomeAndLiving";
import Beauty from "../views/category/Beauty";
import Health from "../views/category/Health";
import WomenShoes from "../views/category/WomenShoes";
import WomenBags from "../views/category/WomenBags";
import FashionAccessories from "../views/category/FashionAccessories";
import Grocery from "../views/category/Grocery";
import BookAndStationery from "../views/category/BookAndStationery";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/products",
    name: "products",
    component: ProductPage,
  },
  {
    path: "/product/:productId",
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
    path: "/men-clothes",
    name: "menClothes",
    component: MenClothes,
  },
  {
    path: "/mobile-and-gadgets",
    name: "mobileAndGadgets",
    component: MobileAndGadgets,
  },
  {
    path: "/consumer-electronics",
    name: "consumerElectronics",
    component: ConsumerElectronics,
  },
  {
    path: "/computer-and-accessories",
    name: "computerAndAccessories",
    component: ComputerAndAccessories,
  },
  {
    path: "/cameras",
    name: "cameras",
    component: Cameras,
  },
  {
    path: "/watches",
    name: "watches",
    component: Watches,
  },
  {
    path: "/men-shoes",
    name: "menShoes",
    component: MenShoes,
  },
  {
    path: "/home-appliances",
    name: "homeAppliances",
    component: HomeAppliances,
  },
  {
    path: "/sport-and-outdoor",
    name: "sportAndOutdoor",
    component: SportAndOutdoor,
  },
  {
    path: "/automotive",
    name: "automotive",
    component: Automotive,
  },
  {
    path: "/women-clothes",
    name: "womenClothes",
    component: WomenClothes,
  },
  {
    path: "/moms-kids-and-babies",
    name: "momsKidsAndBabies",
    component: MomsKidsAndBabies,
  },
  {
    path: "/home-and-living",
    name: "homeAndLiving",
    component: HomeAndLiving,
  },
  {
    path: "/beauty",
    name: "beauty",
    component: Beauty,
  },
  {
    path: "/health",
    name: "health",
    component: Health,
  },
  {
    path: "/women-shoes",
    name: "womenShoes",
    component: WomenShoes,
  },
  {
    path: "/women-bags",
    name: "womenBags",
    component: WomenBags,
  },
  {
    path: "/fashion-accessories",
    name: "fashionAccessories",
    component: FashionAccessories,
  },
  {
    path: "/grocery",
    name: "grocery",
    component: Grocery,
  },
  {
    path: "/books-and-stationery",
    name: "bookAndStationery",
    component: BookAndStationery,
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
