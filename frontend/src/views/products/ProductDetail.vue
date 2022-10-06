<template>
  <div class="product-detail">
    <header-component />
    <product-overview />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductOverview from "@/components/ProductOverview/ProductOverview";

export default {
  name: "ProductDetailPage",
  data: function () {},
  components: {
    HeaderComponent,
    ProductOverview,
  },
};
</script>

<style lang="scss" scoped>
.product-detail {
  background-color: #f5f5f5;
}
</style>
