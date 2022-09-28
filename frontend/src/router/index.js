import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "../views/home/HomePage.vue";
import LoginPage from "../views/auth/LoginPage.vue";
import RegisterPage from "../views/auth/RegisterPage.vue";
import ForgotPasswordPage from "../views/forgot-password/ForgotPasswordPage.vue";
// import FlashcardGamePage from "../views/flashcard-game/FlashcardGamePage.vue";
// import CreateFlashcardPage from "../views/flashcard-game/CreateFlashcardPage.vue";
// import FlashcardCollectionPage from "../views/flashcard-game/FlashcardCollectionPage.vue";
import AccountPage from "../views/user/AccountPage";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  // {
  //   path: "/flashcard-game",
  //   name: "flashcardGame",
  //   component: FlashcardGamePage,
  // },
  // {
  //   path: "/create-flashcard",
  //   name: "createFlashcard",
  //   component: CreateFlashcardPage,
  // },
  // {
  //   path: "/flashcard-collection",
  //   name: "flashcardCollection",
  //   component: FlashcardCollectionPage,
  // },
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
