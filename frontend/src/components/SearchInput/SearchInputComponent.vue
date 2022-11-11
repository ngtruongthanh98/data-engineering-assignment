<template>
  <div class="search-bar-component">
    <el-autocomplete
      :placeholder="placeholder"
      v-model="dataInput"
      :fetch-suggestions="querySearch"
      :trigger-on-focus="false"
      @select="handleSelect"
      class="search-bar-component__input"
    >
      <i slot="prefix" class="el-input__icon el-icon-search"></i>
    </el-autocomplete>

    <template>
      <el-select
        v-model="filterValue"
        placeholder="Select"
        class="search-bar-component__dropdown"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </template>
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
      options: [
        {
          value: "ProductName",
          label: "Product Name",
        },
        {
          value: "CategoryName",
          label: "Category Name",
        },
        {
          value: "SubcategoryName",
          label: "Subcategory Name",
        },
      ],
      filterValue: "ProductName",
      resultData: [],
      label: "",
    };
  },
  methods: {
    querySearch(queryString, cb) {
      var links = this.links;
      // var links = this.resultData;

      var results = queryString
        ? links.filter(this.createFilter(queryString))
        : links;

      // var top5 = results.slice(0, 5);
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
    handleSelect(item) {
      console.log(item);
    },
    // loadAll() {
    //   return [
    //     { value: "vue", link: "https://github.com/vuejs/vue" },
    //     { value: "element", link: "https://github.com/ElemeFE/element" },
    //     { value: "cooking", link: "https://github.com/ElemeFE/cooking" },
    //     { value: "mint-ui", link: "https://github.com/ElemeFE/mint-ui" },
    //     { value: "vuex", link: "https://github.com/vuejs/vuex" },
    //     { value: "vue-router", link: "https://github.com/vuejs/vue-router" },
    //     { value: "babel", link: "https://github.com/babel/babel" },
    //   ];
    // },
    async getProducts(queryParams) {
      // const errorMessage = {
      //   type: "error",
      //   message: "Cannot fetch data",
      // };

      try {
        const resp = await getProducts(queryParams);
        const results = [
          { value: "vue", link: "https://github.com/vuejs/vue" },
          { value: "element", link: "https://github.com/ElemeFE/element" },
          { value: "cooking", link: "https://github.com/ElemeFE/cooking" },
          { value: "mint-ui", link: "https://github.com/ElemeFE/mint-ui" },
          { value: "vuex", link: "https://github.com/vuejs/vuex" },
          { value: "vue-router", link: "https://github.com/vuejs/vue-router" },
          { value: "babel", link: "https://github.com/babel/babel" },
        ];

        if (resp.data.Item) {
          console.log("resp.data: ", resp.data.Item.ProductName?.S);

          results.push({
            value: resp.data.Item.ProductName.S,
            link: "",
          });
        }

        // results.push({
        //   value: resp.data?.Item?.productName?.S,
        //   link: "",
        // });

        this.links = results;
      } catch (error) {
        console.log({ error });
        // this.$message(errorMessage);
      }
    },
    boundedSearch() {
      setTimeout(() => {
        if (!this.dataInput) {
          return;
        }

        this.getProducts({
          [this.filterValue]: this.dataInput,
        });
      }, 300);
    },
  },
  mounted() {
    // this.links = this.loadAll();
  },
  watch: {
    dataInput: function () {
      this.boundedSearch();
    },
    filterValue: function (val) {
      this.dataInput = "";
      if (val === "ProductName") {
        this.placeholder = "Search by name";
      } else if (val === "CategoryName") {
        this.placeholder = "Search by category";
      } else if (val === "SubcategoryName") {
        this.placeholder = "Search by subcategory";
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

.search-bar-component {
  display: flex;
  justify-content: space-between;

  &__input {
    width: 100%;
  }

  &__dropdown {
    margin-left: 20px;
  }
}
</style>