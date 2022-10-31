<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Men Clothes"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { MEN_CLOTHES } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: MEN_CLOTHES,
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