<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Home Appliances"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { HOME_APPLIANCES } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: HOME_APPLIANCES,
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