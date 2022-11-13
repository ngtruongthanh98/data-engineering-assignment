<template>
  <div class="product-detail-page">
    <header-component />
    <product-overview
      :productName="this.productData.productName"
      :imageURL="this.productData.categoryImage"
      :productNumber="this.productData.productNumber"
      :categoryName="this.productData.categoryName"
      :subCategoryName="this.productData.subCategoryName"
      :sellStartDate="this.productData.sellStartDate"
      :sellEndDate="this.productData.sellEndDate"
      :producer="this.productData.producer"
      :price="this.productData.standardCost"
      :quantity="this.productData.safetyStockLevel"
      :productStyle="this.productData.productStyle"
      :rating="this.productData.rating"
    />
    <product-detail
      :productName="this.productData.productName"
      :categoryName="this.productData.categoryName"
      :subCategoryName="this.productData.subCategoryName"
      :brand="this.productData.brand"
      :language="this.productData.language"
      :culture="this.productData.culture"
      :producer="this.productData.producer"
      :sellStartDate="this.productData.sellStartDate"
      :sellEndDate="this.productData.sellEndDate"
      :quantity="this.productData.safetyStockLevel"
      :weight="this.productData.weight"
      :title="this.productData.title"
      :documentLevel="this.productData.documentLevel"
      :owner="this.productData.owner"
      :status="this.productData.status"
      :documnentSummary="this.productData.documnentSummary"
    />
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

import { getProducts } from "@/services/products";

export default {
  name: "ProductDetailPage",
  data() {
    return {
      productData: {},
    };
  },
  components: {
    HeaderComponent,
    ProductOverview,
    ProductDetail,
    ProductRating,
    Copyright,
  },
  methods: {
    async getProductDetail(queryParams) {
      try {
        const resp = await getProducts(queryParams);

        this.productData = resp.data;

        console.log("productData: ", this.productData);
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    const productName = this.$route.params.productName;
    const queryParams = {
      ProductName: productName,
    };

    this.getProductDetail(queryParams);
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: $color-gray;
}
</style>
