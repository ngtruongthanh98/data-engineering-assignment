<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="copyright-info">
    <div class="copyright-info__inner">Copyright by ThanhNT26</div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.copyright-info {
  width: 100%;
  margin-top: auto;
  min-height: 60px;
  z-index: 1;

  display: flex;
  justify-content: center;

  &__inner {
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 18px;
    color: $color-low-contract;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>