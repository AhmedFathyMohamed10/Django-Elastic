<template>
  <div class="row">
    <div class="mic">
      <div class="col-12">
        <CustomTabs class="text-center" v-model="selectedTab" :tabs="tabs">
        </CustomTabs>
      </div>
      <div class="col-12">
        <CustomTabs class="text-center" v-model="DrugTab" :tabs="search_drug_tabs">
        </CustomTabs>
        <Base>
        <!-- Search bar -->
        <div class="search-container mt-4">
          <p class="search-title">Search for Drugs</p>
          <span class="p-input-icon-right">
            <input type="text" v-model="searchQuery" @input="debouncedSearch" placeholder="Search..."
              class="p-inputtext p-component" />
            <i class="pi pi-search" @click="search"></i>
          </span>
        </div>
        </Base>
        <!-- For loading or errors only -->
        <div v-if="loading || error">
          <Loader v-if="loading" />
          <div v-if="error" class="error">{{ error }}</div>
        </div>

        <!-- Drug information section -->
        <div v-if="filteredDrugResults.length > 0" class="scroll-container">
          <ul>
            <li v-for="(drug, index) in filteredDrugResults" :key="index" class="drug-info mt-4"
              @click="selectDrug(drug)">
              <span>{{ drug.openfda.brand_name && drug.openfda.brand_name.join(', ') || drug.openfda.generic_name &&
                drug.openfda.generic_name.join(', ') }}</span>
            </li>
          </ul>
        </div>

        <div class="pagination-controls mt-4">
          <button @click="prevPage" :disabled="page === 1">Previous</button>
          <span>Page {{ page }}</span>
          <button @click="nextPage" :disabled="!hasMoreResults">Next</button>
        </div>

        <!-- Selected drug details section -->
        <div v-if="selectedDrug" class="selected-drug-info mt-4">
          <Base>
          <h5 class="drug-name">{{ selectedDrug.openfda.brand_name && selectedDrug.openfda.brand_name.join(', ') ||
            selectedDrug.openfda.generic_name && selectedDrug.openfda.generic_name.join(', ') }}</h5>
          <hr>
          <div class="row">
            <div class="col-md-6 field-name">
              <p v-if="selectedDrug.openfda.brand_name">Brand Name</p>
              <p v-if="selectedDrug.openfda.generic_name">Generic Name</p>
              <p v-if="selectedDrug.openfda.manufacturer_name">Manufacturer Name</p>
              <p v-if="selectedDrug.openfda.application_number">Application Number</p>
              <p v-if="selectedDrug.openfda.product_type">Product Type</p>
              <p v-if="selectedDrug.openfda.route">Route</p>
              <p v-if="selectedDrug.openfda.substance_name">Substance Name</p>
              <p v-if="selectedDrug.openfda.rxcui">RxCUI</p>
            </div>
            <div class="col-md-6 field-value">
              <div v-if="selectedDrug.openfda.brand_name">
                <span v-for="(name, idx) in selectedDrug.openfda.brand_name" :key="'brand_name_' + idx">- {{ name
                  }}</span>
              </div>
              <div v-if="selectedDrug.openfda.generic_name">
                <span v-for="(name, idx) in selectedDrug.openfda.generic_name" :key="'generic_name_' + idx">- {{ name
                  }}</span>
              </div>
              <div v-if="selectedDrug.openfda.manufacturer_name">
                <span v-for="(name, idx) in selectedDrug.openfda.manufacturer_name" :key="'manufacturer_name_' + idx">-
                  {{ name }}</span>
              </div>
              <div v-if="selectedDrug.openfda.application_number">
                <span v-for="(name, idx) in selectedDrug.openfda.application_number"
                  :key="'application_number_' + idx">- {{ name }}</span>
              </div>
              <div v-if="selectedDrug.openfda.product_type">
                <span v-for="(name, idx) in selectedDrug.openfda.product_type" :key="'product_type_' + idx">- {{ name
                  }}</span>
              </div>
              <div v-if="selectedDrug.openfda.route">
                <span v-for="(name, idx) in selectedDrug.openfda.route" :key="'route_' + idx">- {{ name }}</span>
              </div>
              <div v-if="selectedDrug.openfda.substance_name">
                <span v-for="(name, idx) in selectedDrug.openfda.substance_name" :key="'substance_name_' + idx">- {{
                  name }}</span>
              </div>
              <div v-if="selectedDrug.openfda.rxcui">
                <span v-for="(name, idx) in selectedDrug.openfda.rxcui" :key="'rxcui_' + idx">- {{ name }}</span>
              </div>
            </div>
          </div>
          </Base>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CustomTabs from "@/components/global/custom/CustomTabs.vue";
import Loader from "@/components/global/utilities/Loader.vue";
import Base from "@/components/global/utilities/Base.vue";
import axios from 'axios';
import { debounce } from 'lodash';

export default {
  name: "searchDrug",
  components: {
    CustomTabs,
    Base,
    Loader,
  },
  data() {
    return {
      selectedTab: "humanDrugs",
      tabs: [
        { en: "Human Drugs", ar: "أدوية بشرية", key: "humanDrugs" },
        { en: "Animal Drugs", ar: "أدوية حيوانية", key: "animalDrugs" },
        { en: "Procedures", ar: "إجراءات", key: "procedures" },
        { en: "Devices", ar: "أجهزة", key: "devices" },
        { en: "Food", ar: "طعام", key: "food" },
        { en: "News", ar: "أخبار", key: "news" },
      ],
      DrugTab: "drugProfile",
      search_drug_tabs: [
        { en: "Drug Profile", ar: "ملف الدواء", key: "drugProfile" },
        { en: "Drug Interaction", ar: "تفاعل الدواء", key: "drugInteraction" },
        { en: "Pill Identifier", ar: "معرف الحبة", key: "pillIdentifier" },
        { en: "Comparisons", ar: "مقارنات", key: "comparisons" },
      ],
      searchQuery: "",
      drugResults: [],
      page: 1,
      pageSize: 10,
      hasMoreResults: false,
      loading: false,
      error: null,
      selectedDrug: null
    };
  },
  created() {
    this.debouncedSearch = debounce(this.search, 300);
  },
  computed: {
    filteredDrugResults() {
      return this.drugResults.filter(drug => drug.openfda.brand_name || drug.openfda.generic_name);
    }
  },
  methods: {
    async search() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('/drugs/', {
          params: {
            search: this.searchQuery,
            page: this.page,
            pageSize: this.pageSize
          },
          headers: {
            'Content-type': 'application/json',
            'lang': 'en',
          }
        });
        this.drugResults = response.data.results;
        this.hasMoreResults = response.data.next !== null;
      } catch (error) {
        console.error("There was an error with the search request:", error);
        this.error = "There was an error with the search request. Please try again.";
      } finally {
        this.loading = false;
      }
    },
    prevPage() {
      if (this.page > 1) {
        this.page--;
        this.search();
      }
    },
    nextPage() {
      if (this.hasMoreResults) {
        this.page++;
        this.search();
      }
    },
    selectDrug(drug) {
      this.selectedDrug = drug;
    }
  }
};
</script>

<style scoped lang="scss">
div.mic {
  background-color: white;
  padding: 10px;
  margin-top: 9px;
  border: 2px solid white;
  border-radius: 8px;
  margin-left: 5px;
}

.search-container {
  text-align: center;
  margin-top: 1rem;
}

.search-title {
  font-size: 0.875rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.p-input-icon-right {
  width: 50% !important;
}

.scroll-container {
  max-height: 200px;
  overflow-y: auto;
}

.drug-info {
  text-align: center;
  margin-top: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #c9c9c9;
  }
}

.drug-name {
  font-size: 1.2rem;
  font-weight: 700;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
  transition: background-color 0.2s;
}

li:hover {
  background-color: #f0f0f0;
}

.field-name p {
  margin: 0;
  color: #000000 !important;
  font-size: small;
  font-weight: bold;
}

.field-value p {
  margin: 0;
  color: #56C596 !important;
  font-size: small;
  font-weight: 500;
}

.row {
  display: flex;
  justify-content: space-between;
}

.field-name {
  border-right: 1px solid #ccc;
  padding-right: 1rem;
}

.field-value {
  padding-left: 1rem;
}

hr {
  margin: 1rem 0;
  border: 0;
  height: 3px;
  background-color: #18ac7d;
}

.pagination-controls {
  text-align: center;
  margin-top: 1rem;

  button {
    background-color: #18ac7d;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;

    &:hover {
      background-color: #0d8a5b;
    }

    &:disabled {
      background-color: #ccc;
      cursor: not-allowed;
    }
  }

  span {
    font-size: 1rem;
    font-weight: bold;
  }
}

.error {
  color: rgb(241, 54, 54);
  text-align: center;
}

.selected-drug-info {
  margin-top: 2rem;
}
</style>
