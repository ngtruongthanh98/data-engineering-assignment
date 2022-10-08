<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Computer & Accessories"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { COMPUTER_AND_ACCESSORIES } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: COMPUTER_AND_ACCESSORIES,
    };
  },
  components: {
    HeaderComponent,
    SubCategoryComponent,
  },
};
</script>

<style lang="scss">
.category {
}
</style>