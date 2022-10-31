<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Home & Living"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { HOME_AND_LIVING } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: HOME_AND_LIVING,
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