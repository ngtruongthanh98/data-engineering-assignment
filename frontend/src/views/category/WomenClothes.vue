<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Women Clothes"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { WOMEN_CLOTHES } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: WOMEN_CLOTHES,
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