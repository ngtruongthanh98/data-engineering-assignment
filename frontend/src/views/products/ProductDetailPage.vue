<template>
  <div class="product-detail-page">
    <header-component />
    <product-overview
      :productName="this.productData.productName"
      :imageURL="this.productData.categoryImage || this.noDataImage"
      :productNumber="this.productData.productID"
      :categoryName="this.productData.categoryName"
      :subCategoryName="this.productData.subCategoryName"
      :sellStartDate="this.productData.partnerItemCreated"
      :sellEndDate="this.productData.sellEndDate"
      :producer="this.productData.identityItemBrand"
      :price="this.productData.standardCost"
      :quantity="this.productData.partnerItemQty"
      :productStyle="this.productData.productStyle"
      :rating="this.productData.rating"
    />
    <product-detail
      :productName="this.productData.productName"
      :categoryName="this.productData.categoryName"
      :subCategoryName="this.productData.subCategoryName"
      :brand="this.productData.identityItemBrand"
      :language="this.productData.language"
      :culture="this.productData.culture"
      :producer="this.productData.identityItemBrand"
      :sellStartDate="this.productData.partnerItemCreated"
      :sellEndDate="this.productData.sellEndDate"
      :quantity="this.productData.partnerItemQty"
      :weight="this.productData.weight"
      :title="this.productData.title"
      :documentLevel="this.productData.documentLevel"
      :owner="this.productData.owner"
      :status="this.productData.status"
      :documnentSummary="this.productData.identityItemDescription"
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
      noDataImage: require("@/assets/No_Image_Available.jpg"),
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

        this.productData = resp.data.data[0] || resp.data.data;

        console.log("productData: ", this.productData);
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    const productName = this.$route.path.split("/")[2];

    console.log("productName: ", productName);

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
