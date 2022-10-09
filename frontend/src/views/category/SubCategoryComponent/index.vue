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

export default {
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
};
</script>

<style lang="scss">
.sub-category-container {
  .title {
    padding: 0.5rem 0.625rem 0.5rem 0.75rem;
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