<template>
  <el-row class="header-component">
    <el-col :span="8" class="navbar__logo-box">
      <img
        src="@/assets/aws_logo.png"
        alt=""
        class="navbar__logo"
        @click="onClickLogo"
      />
    </el-col>
    <el-col v-if="isShowSearchBar" :span="8" class="navbar_search-box">
      <search-input-component />
    </el-col>
    <el-col :span="8" class="navbar__menu-box">
      <ul class="el-menu el-menu--horizontal navbar__menu">
        <li class="el-menu-item">
          <router-link to="/">Home</router-link>
        </li>
        <li class="el-menu-item">
          <router-link to="/product">Products</router-link>
        </li>
        <li class="el-menu-item account-setting-box">
          <el-dropdown trigger="click" v-on:command="handleNavDropdownCommand">
            <span class="el-dropdown-link account-setting"
              >thanhnt26<i class="el-icon-caret-bottom el-icon--right"></i
            ></span>
            <el-dropdown-menu slot="dropdown" class="navbar__dropdown-menu">
              <el-dropdown-item
                ><router-link to="/user/account"
                  >Account</router-link
                ></el-dropdown-item
              >
              <el-dropdown-item command="logout" divided
                >Logout</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
        </li>
      </ul>
    </el-col>
  </el-row>
</template>

<script>
import SearchInputComponent from "../SearchInput/SearchInputComponent.vue";
export default {
  data() {
    return {};
  },
  props: {
    isShowSearchBar: {
      type: Boolean,
      default: true,
    },
  },
  components: {
    SearchInputComponent,
  },
  methods: {
    handleNavDropdownCommand: function (command) {
      if (command == "logout") {
        this.$confirm("Do you want to logout?", "Notification", {
          confirmButtonText: "Logout",
          cancelButtonText: "Cancel",
          type: "warning",
        }).then(
          function () {
            this.$message("Logout successfully");
          }.bind(this)
        );
      }
    },
    goTo(route) {
      this.$router.push({ name: route });
    },
    onClickLogo() {
      this.goTo("home");
    },
  },
};
</script>
<style lang="scss" scoped>
.header-component {
  padding: 10px 0;
  background: $color-header-background;
}

.navbar__logo-box {
  background-color: transparent;
}
.navbar__logo {
  display: block;
  height: 60px;
  margin-left: 48px;
  cursor: pointer;
}
.navbar_search-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 60px;
}
.navbar__menu-box {
  background-color: transparent;
}
.navbar__menu {
  float: right;
  background-color: transparent;
  box-shadow: none;
  border-bottom: unset;
  margin-right: 28px;

  .el-menu-item {
    color: $color-white;

    &:hover {
      background-color: transparent;
      color: hsla(0, 0%, 100%, 0.7);
    }

    .account-setting {
      color: $color-white;
    }
  }
}

.account-setting-box {
  .account-setting {
    &:hover {
      color: hsla(0, 0%, 100%, 0.7);
    }
  }
}
.navbar__dropdown-menu a {
  color: inherit;
  text-decoration: none !important;
}
.navbar__title {
  margin-top: 0;
  margin-bottom: 0;
  margin-left: 12px;
  height: 60px;
  line-height: 60px;
  font-size: 1.5em;
  font-weight: bold;
}
.navbar__title a {
  color: #48576a;
  text-decoration: none !important;
}
.el-menu-item a {
  text-decoration: none !important;
}
</style>