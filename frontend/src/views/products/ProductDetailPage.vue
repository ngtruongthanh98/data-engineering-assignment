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
    <product-rating :rating="this.productData.rating" />

    <div v-if="similarProduct.length > 0" class="product-similar">
      <div class="product-similar-header">Maybe you like</div>
      <div class="product-similar-body">
        <product-item
          v-for="(product, index) in similarProduct"
          :key="index"
          :product-data-overview="product"
        />
      </div>
    </div>

    <!-- <el-pagination
        class="pagination-box"
        small
        layout="prev, pager, next"
        :total="50"
      >
      </el-pagination> -->
    <copyright />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductOverview from "@/components/ProductOverview/ProductOverview";
import ProductDetail from "@/components/ProductDetail/ProductDetail";
import ProductRating from "@/components/ProductRating/ProductRating";
import Copyright from "@/components/Copyright";
import ProductItem from "@/views/category/SubCategoryComponent/ProductItem/index";

import { getProducts } from "@/services/products";

export default {
  name: "ProductDetailPage",
  data() {
    return {
      productData: {},
      similarProduct: [],
      noDataImage: require("@/assets/No_Image_Available.jpg"),
    };
  },
  components: {
    HeaderComponent,
    ProductOverview,
    ProductDetail,
    ProductRating,
    ProductItem,
    Copyright,
  },
  methods: {
    async getProductDetail(queryParams) {
      try {
        const resp = await getProducts(queryParams);

        this.productData = resp.data.data[0] || resp.data.data;
        const similarProductNames = JSON.parse(
          this.productData.partnerItemPackageItemIds
        );
        this.similarProduct = await Promise.all(
          similarProductNames.map(
            async (sp) => (await getProducts({ ProductName: sp })).data.data[0]
          )
        );
        console.log("productData: ", this.similarProduct);
      } catch (error) {
        console.log(error);
      }
    },
  },
  watch: {
    $route() {
      const queryParams = {
        ProductName: this.$route.params.productName,
      };
      this.getProductDetail(queryParams);
    },
  },
  mounted() {
    const productName = this.$route.path.split("/")[2];

    const queryParams = {
      ProductName: productName.replace(/%20/g, " "),
    };

    this.getProductDetail(queryParams);
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: $color-gray;
}

.product-similar {
  &-header {
    background-color: $color-white;
    text-align: start;
    padding: 24px;
    font-weight: bold;
  }
  padding: 24px 200px 0px 200px;
  &-body {
    padding: 24px;
    background-color: $color-white;
    display: flex;
    align-items: flex-start;

    // .title {
    //   font-size: 18px;
    //   padding: 24px;
    //   text-align: start;
    // }
  }
}
</style>
