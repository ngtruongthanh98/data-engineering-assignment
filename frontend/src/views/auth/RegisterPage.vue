<template>
  <div class="register-page">
    <h1>Register Page</h1>

    <el-form
      :label-position="labelPosition"
      label-width="100px"
      :model="registerForm"
    >
      <el-form-item label="Username">
        <el-input v-model="registerForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="registerForm.password" type="password"></el-input>
      </el-form-item>
      <el-form-item label="Connfirm Password">
        <el-input
          v-model="registerForm.connfirmPassword"
          type="password"
        ></el-input>
      </el-form-item>

      <el-link href="http://localhost:8080/login">Login</el-link>

      <el-form-item>
        <el-button type="primary" @click="submitForm('dynamicValidateForm')"
          >Register</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "RegisterPage",
  components: {},
  data() {
    return {
      input: "",
      labelPosition: "right",
      registerForm: {
        username: "",
        password: "",
        connfirmPassword: "",
      },
    };
  },
  methods: {
    submitForm(registerForm) {
      console.log(registerForm);
    },
  },
};
</script>