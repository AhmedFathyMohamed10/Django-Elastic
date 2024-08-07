<template>
  <div class="mic">
    <div class="col-12">
      <CustomTabs class="text-center" v-model="selectedTab" :tabs="tabs" />
    </div>

    <div class="col-12">
      <CustomTabs class="text-center" v-model="DrugTab" :tabs="search_drug_tabs" />
      <!-- Search bar -->
      <div class="search-container mt-4">
        <p class="search-title">Search for Drug</p>
        <span class="p-input-icon-right">
          <input type="text" v-model="searchQuery" @input="debouncedSearch" placeholder="Search..." class="p-inputtext p-component" />
          <i class="pi pi-search" @click="search"></i>
        </span>
      </div>

      <!-- For loading or errors only -->
      <div v-if="loading || error">
        <Loader v-if="loading" />
        <div v-if="error" class="error">{{ error }}</div>
      </div>

      <Base>
        <h4 class="mb-0">Drugs List</h4>
        <!-- Search results -->
        <div class="search-results" v-if="searchResults.length > 0">
          <ul>
            <li v-for="(drug, index) in searchResults" :key="index" @click="selectDrug(drug)">
              {{ (drug.openfda?.brand_name?.join(', ') || '') | capFirst }} ⬌ {{ (drug.openfda?.generic_name?.join(', ') || '') | capFirst }}
            </li>
          </ul>
        </div>
        <!-- Added drugs list -->
        <div class="added-drugs" v-if="addedDrugs.length > 0">
          <ul>
            <li v-for="(drug, index) in addedDrugs" :key="index">
              <Button :label="(drug.openfda?.brand_name?.join(', ') || '') | capFirst" icon="pi pi-times" iconPos="right" @click="removeDrug(index)" class="remove-button" />
            </li>
          </ul>
          <div class="actions">
            <button class="btn btn-success-gradient btn-pill" @click="checkInteractions">Check</button>
            <button class="btn btn-secondary-gradient btn-pill">Save</button>
            <button class="btn btn-secondary-gradient btn-pill" disabled>Saved List</button>
          </div>
        </div>
      </Base>

      <Base>
        <h4 class="mb-0">Drug Interaction Report</h4>
        <div v-if="interactionResults && interactionResults.length > 1" class="interaction-results">
          <p v-if="addedDrugs.length > 1">
            There {{ interactionResults.length > 1 ? 'are' : 'is' }} <strong class="length-interactions">{{ interactionResults.length }}</strong> potential interaction{{ interactionResults.length > 1 ? 's' : '' }} between the selected drugs.
          </p>
          <ul v-if="addedDrugs.length > 1">
            <li v-for="(interaction, index) in interactionResults" :key="index">
              <strong class="drug">{{ interaction.drug1 | capFirst }}</strong> interacts with <strong class="drug">{{ interaction.drug2 | capFirst }}</strong>
              <p>⬌ {{ interaction.description || 'No description available' | capFirst }}</p>
            </li>
          </ul>
          <div v-else>
            <p>
              The selected drug interacts with <strong class="length-interactions">{{ interactionResults.length }}</strong> other drug{{ interactionResults.length > 1 ? 's' : '' }}.
            </p>
            <ul>
              <li v-for="(interaction, index) in interactionResults" :key="index">
                <strong class="drug-name">{{ interaction.name | capFirst }}</strong>
                <!-- Display multiple descriptions if available -->
                <ul>
                  <li v-for="(desc, idx) in interaction.descriptions" :key="idx">
                    <p>⬌ {{ desc || 'No description available' | capFirst }}</p>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
        <div v-if="interactionResults.length === 0 && interactionMessage" class="interaction-message">
          <p class="no-interactions">{{ interactionMessage | capFirst }}</p>
        </div>
      </Base>
    </div>
  </div>
</template>

<script>
import CustomTabs from "@/components/global/custom/CustomTabs.vue";
import Base from "@/components/global/utilities/Base.vue";
import Loader from "@/components/global/utilities/Loader.vue";
import axios from 'axios';
import { debounce } from 'lodash';

export default {
  name: 'InteractionsDrugs',

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
      searchResults: [],
      addedDrugs: [],
      loading: false,
      error: null,
      interactionResults: [],
      interactionMessage: null
    }
  },

  created() {
    this.debouncedSearch = debounce(this.search, 300);
  },

  methods: {
    async search() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('/drugs/', {
          params: { search: this.searchQuery },
          headers: { 'Content-Type': 'application/json', 'lang': 'en' }
        });
        this.searchResults = response.data.results;
      } catch (error) {
        console.error("There was an error with the search request:", error);
        this.error = "There was an error with the search request. Please try again.";
      } finally {
        this.loading = false;
      }
    },

    addDrug() {
      const selectedDrug = this.searchResults.find(drug =>
        drug.openfda?.brand_name?.some(name => name.toLowerCase() === this.searchQuery.toLowerCase()) ||
        drug.openfda?.generic_name?.some(name => name.toLowerCase() === this.searchQuery.toLowerCase())
      );
      if (selectedDrug && !this.addedDrugs.includes(selectedDrug)) {
        this.addedDrugs.push(selectedDrug);
      }
    },

    selectDrug(drug) {
      if (!this.addedDrugs.includes(drug)) {
        this.addedDrugs.push(drug);
      }
      this.searchResults = [];
      this.searchQuery = '';
    },

    removeDrug(index) {
      this.addedDrugs.splice(index, 1);
    },

    async checkInteractions() {
      try {
        if (this.addedDrugs.length < 1) {
          this.error = "Please add at least one drug to check interactions.";
          return;
        }

        const requestData = this.addedDrugs.map(drug =>
          (drug.openfda?.generic_name || drug.openfda?.brand_name || []).join(', ')
        );
        console.log('Request data:', requestData);

        const response = await axios.post('/check-drug-interactions/', { drugs: requestData });
        console.log('Response data:', response.data);

        // Check if the backend returns interaction results
        if (response.data.interactions) {
          if (this.addedDrugs.length === 1) {
            // Handle the case for one drug
            if (response.data.drug1_length === 0) {
              this.interactionMessage = 'No drug interactions were found for this drug. However, this does not necessarily mean no interactions exist. Always consult your healthcare provider.';
            } else {
              this.interactionResults = (response.data.drug_interactions || []).slice(0, 10);
              this.interactionMessage = response.data.message || 'No interactions found.';
            }
          } else {
            // Handle the case for multiple drugs
            this.interactionResults = (response.data.details || []).slice(0, 10);
            this.interactionMessage = response.data.message || 'No interactions found.';
          }
        } else {
          this.interactionResults = [];
          this.interactionMessage = response.data.message || 'No interactions found.';
        }

        console.log('Interaction results:', this.interactionResults);
      } catch (error) {
        console.error("There was an error checking the drug interactions:", error);
        this.error = "There was an error checking the drug interactions. Please try again.";
      }
    },
  },
}
</script>

<style scoped>
div.mic {
  background-color: white;
  padding: 10px;
  margin-top: 9px;
  border: 2px solid white;
  border-radius: 8px;
}

.search-container {
  text-align: center;
  margin-top: 1rem;
}

.search-title {
  color: black;
  font-size: 0.875rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.p-input-icon-right {
  width: 50% !important;
}

.search-results {
  max-height: 200px;
  overflow-y: auto;
  margin-top: 0.5rem;
  border: 1px solid #59e159;
  border-radius: 4px;
  /* Rounded corners for a modern look */
  background-color: #fff;
  /* Background color for better visibility */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* Subtle shadow for depth */
}

.search-results ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.search-results li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  /* Light border for separation */
  cursor: pointer;
  /* Pointer cursor to indicate clickable items */
  transition: background-color 0.2s;
  /* Smooth background color transition */
}

.search-results li:hover {
  background-color: #f0f0f0;
  /* Light gray background on hover */
}

.search-results li:last-child {
  border-bottom: none;
  /* Remove border from the last item */
}

.added-drugs {
  margin-top: 1rem;
}

.added-drugs ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  /* Space between blocks */
}

.added-drugs li {
  padding: 0.5rem 1rem;
  border-radius: 1rem;
  /* Rounded corners */
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10px;
  width: auto;
  margin-bottom: 10px;
}

.remove-button .pi-times {
  color: red;
}

.actions {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.actions .btn {
  flex: 1;
  margin: 0 5px;
}

.length-interactions {
  color: red;
  font-size: large;
  font-weight: 400;
}

button.btn-pill {
  border-radius: 25px;
  margin-bottom: 20px;
  margin-left: 10px;
}

.interaction-results {
  margin-top: 1rem;
}

.interaction-results ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.interaction-results li {
  padding: 0.5rem;
}

.interaction-message {
  margin-top: 1rem;
  font-weight: bold;
}

p {
  margin: 0;
  font-weight: 450;
  font-size: 15px;
  color: rgb(13, 0, 160)
}

.drug-name {
  font-weight: 750;
  font-size: 18px;
  color: rgb(0, 0, 0)
}

.drug {
  color: red;
  font-size: large;
}

p.no-interactions {
  margin: 0;
  font-weight: 450;
  font-size: 15px;
  color: rgb(13, 0, 160)
}
</style>
