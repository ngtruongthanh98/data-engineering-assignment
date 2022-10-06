<template>
  <div class="product-page">
    <header-component />
    <h1>Products</h1>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";

export default {
  name: "ProductPage",
  data: function () {
    return {};
  },
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss" scoped>
.product-page {
  color: $color-primary;
}
</style>
