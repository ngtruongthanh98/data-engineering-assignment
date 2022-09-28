<template>
  <div class="home">
    <header-component />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent.vue";

export default {
  name: "HomePage",
  data: function () {
    return {};
  },
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss" scoped>
.home {
  color: $color-primary;
}
</style>
