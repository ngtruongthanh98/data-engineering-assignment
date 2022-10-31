<template>
  <div class="product-detail-page">
    <header-component />
    <product-overview />
    <product-detail />
    <product-rating />
    <copyright />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductOverview from "@/components/ProductOverview/ProductOverview";
import ProductDetail from "@/components/ProductDetail/ProductDetail";
import ProductRating from "@/components/ProductRating/ProductRating";
import Copyright from "@/components/Copyright";

export default {
  name: "ProductDetailPage",
  // data: function () {},
  components: {
    HeaderComponent,
    ProductOverview,
    ProductDetail,
    ProductRating,
    Copyright,
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: $color-gray;
}
</style>
