<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Women Bags"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { WOMEN_BAGS } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: WOMEN_BAGS,
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