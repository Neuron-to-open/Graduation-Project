/// <reference types="vite/client" />

import { type IStaticMethods } from "preline/preline"
declare global {
  interface Window {
    HSStaticMethods: IStaticMethods
  }
}

declare module "*.vue" {
  import { ComponentOptions } from "vue";
  const componentOptions: ComponentOptions;
  export default componentOptions;
}
