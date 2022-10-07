<template>
  <div class="product-detail-page">
    <header-component />
    <product-overview />
    <product-detail />
    <product-rating />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductOverview from "@/components/ProductOverview/ProductOverview";
import ProductDetail from "@/components/ProductDetail/ProductDetail";
import ProductRating from "@/components/ProductRating/ProductRating";

export default {
  name: "ProductDetailPage",
  // data: function () {},
  components: {
    HeaderComponent,
    ProductOverview,
    ProductDetail,
    ProductRating,
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: #f5f5f5;
}
</style>
