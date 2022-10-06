<template>
  <div class="product-detail-page">
    <header-component />
    <product-overview />
    <product-detail />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductOverview from "@/components/ProductOverview/ProductOverview";
import ProductDetail from "@/components/ProductDetail/ProductDetail";

export default {
  name: "ProductDetailPage",
  data: function () {},
  components: {
    HeaderComponent,
    ProductOverview,
    ProductDetail,
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: #f5f5f5;
}
</style>
