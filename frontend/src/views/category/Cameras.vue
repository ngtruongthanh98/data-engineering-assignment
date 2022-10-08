<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Cameras"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { CAMERAS } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: CAMERAS,
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