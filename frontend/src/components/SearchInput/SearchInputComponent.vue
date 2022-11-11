<template>
  <div>
    <el-autocomplete
      :placeholder="placeholder"
      v-model="dataInput"
      :fetch-suggestions="querySearch"
      :trigger-on-focus="false"
      @select="handleSelect"
    >
      <i slot="prefix" class="el-input__icon el-icon-search"></i>
    </el-autocomplete>

    <!-- filter dropdown with icon -->
    <el-dropdown
      v-if="filterDropdown"
      class="filter-dropdown"
      @command="handleFilterDropdown"
    >
      <span class="el-dropdown-link">
        <i class="el-icon-caret-bottom"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="all">All</el-dropdown-item>
        <el-dropdown-item command="active">Active</el-dropdown-item>
        <el-dropdown-item command="inactive">Inactive</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import { getProducts } from "@/services/products";
export default {
  data() {
    return {
      links: [],
      dataInput: "",
      placeholder: "Search by name",
    };
  },
  methods: {
    querySearch(queryString, cb) {
      var links = this.links;
      var results = queryString
        ? links.filter(this.createFilter(queryString))
        : links;
      // call callback function to return suggestions
      cb(results);
    },
    createFilter(queryString) {
      return (link) => {
        return (
          link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
    },
    loadAll() {
      return [
        { value: "vue", link: "https://github.com/vuejs/vue" },
        { value: "element", link: "https://github.com/ElemeFE/element" },
        { value: "cooking", link: "https://github.com/ElemeFE/cooking" },
        { value: "mint-ui", link: "https://github.com/ElemeFE/mint-ui" },
        { value: "vuex", link: "https://github.com/vuejs/vuex" },
        { value: "vue-router", link: "https://github.com/vuejs/vue-router" },
        { value: "babel", link: "https://github.com/babel/babel" },
      ];
    },
    handleSelect(item) {
      console.log(item);
    },
    async getProducts(queryParams) {
      const errorMessage = {
        type: "error",
        message: "Cannot fetch data",
      };

      try {
        const resp = await getProducts(queryParams);
        const { status, data } = resp;

        console.log("status: ", status);
        console.log("id: ", data.Item.ProductID.N);
      } catch (error) {
        console.log({ error });
        this.$message(errorMessage);
      }
    },
  },
  mounted() {
    // this.links = this.loadAll();

    const queryParams = {
      // CategoryName: "Clothing",
      ProductName: "HL Nipple",
      // SubcategoryName: "Bike Stands",
    };

    this.getProducts(queryParams);
  },
  watch: {
    dataInput: function (val) {
      console.log(val);

      if (val.length === 0) {
        return;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.search-option {
  // margin-left: 10px;
}

.el-autocomplete {
  display: block;
}
</style>