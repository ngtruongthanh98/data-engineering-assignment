<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Consumer Electronics"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { CONSUMER_ELECTRONICS } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: CONSUMER_ELECTRONICS,
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