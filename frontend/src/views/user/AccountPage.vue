<template>
  <div class="user-account">
    <header-component />
    <h1>User Account</h1>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";

export default {
  name: "UserAccountPage",
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss" scoped>
.user-account {
  color: $color-primary;
}
</style>