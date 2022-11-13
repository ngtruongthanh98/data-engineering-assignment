<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="sub-category-container">
    <h1 class="title">{{ title }}</h1>

    <div class="body">
      <sub-category-list :title="title" :subCategoryList="subCategoryList" />
      <div class="main">
        <product-item />
        <product-item />
        <product-item />
        <product-item />
        <product-item />

        <product-item />
        <product-item />
        <product-item />
        <product-item />
        <product-item />
      </div>
    </div>
  </div>
</template>

<script>
import SubCategoryList from "./SubCategoryList";
import ProductItem from "./ProductItem";
// import { getSubCategories } from "@/services/products";

export default {
  data() {
    return {
      // title: "",
      // subCategoryList: [],
    };
  },
  props: {
    title: {
      type: String,
      default: "",
    },
    subCategoryList: {
      type: Array,
      default: () => [],
    },
  },
  components: {
    SubCategoryList,
    ProductItem,
  },
  methods: {
    // async getSubCategories() {
    //   const queryParams = {
    //     CategoryName: "Accessories",
    //   };
    //   const response = await getSubCategories(queryParams);
    //   console.log("response: ", response);
    //   // this.subCategoryList = response.data.data;
    //   // map response.data.data
    //   this.subCategoryList = response.data.data.map((item) => {
    //     return {
    //       subcategoryName: item.subcategoryName,
    //     };
    //   });
    //   console.log("subCategoryList: ", this.subCategoryList);
    // },
  },
  mounted() {
    // this.getSubCategories("Accessories");
  },
};
</script>

<style lang="scss">
.sub-category-container {
  .title {
    padding: 24px;
    font-size: 18px;
  }
  .body {
    font-size: 14px;
    display: flex;
    margin: 0px 200px 0px 200px;

    .sub-category-list {
      width: 20%;
    }

    .main {
      width: 80%;
      display: grid;
      grid-template-columns: repeat(5, 230px);
      gap: 10px;
    }
  }
}
</style>