<!-- *********************************search clinics************************ -->
<template>
 <div class="content-scroll" > 
    <div class="content-core my-5">
      <!-- /////////testDummyData && dummyData.length<=0///////// -->
      <div class="row position-relative">  
        <!-- /////////////////Filters Small Screen////////////// -->
        <div v-if="hideFilterScreen" class="animate__animated animate__fadeInDown animate__fast  custom-filters-screen">
          <Base>
          <div class="content-filters">
            <div class="d-flex justify-content-between align-items-center">
                <div><h5 class="text-black mb-0"> FILTERS </h5></div>
                <div> <button  @click="closeFilersScreen" class="btn btn-outline-secondary"><i class="fa fa-close"></i></button></div>
            </div>
            <Divider class="m-0"></Divider>
            <div class="accordion accordion-flush background-body" id="accordionFlushExample">
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                    <i class="pi pi-paypal  mx-2"></i>
                    <span class="text-black">Title</span>
                  </button>
                </h2>
                <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Professor" id="Professor" value="Professor"
                        v-model="filters.title">
                      <label class="form-check-label" for="Professor">
                        Professor
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Specialist" checked id="Specialist"
                        value="Specialist" v-model="filters.title">
                      <label class="form-check-label" for="Specialist">
                        Specialist
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                    <i class="fa-solid fa fa-stethoscope fw-bold mx-2"></i><span class="text-black">Sub Specialities</span>
                  </button>
                </h2>
                <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Dentistry" id="Dentistry" value="Dentistry"
                        v-model="filters.specialities">
                      <label class="form-check-label" for="Dentistry">
                        Dentistry
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Dermatology" checked id="Dermatology"
                        value="Dermatology" v-model="filters.specialities">
                      <label class="form-check-label" for="Dermatology">
                        Dermatology
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                    <i class="fa-solid fa fa-venus-mars fw-bold mx-2"></i>
                    <span class="text-black">Gender</span>
                  </button>
                </h2>
                <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Male" id="Male" value="Male"
                        v-model="filters.gender">
                      <label class="form-check-label" for="Male">
                        Male
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Femal" checked id="Femal" value="Femal"
                        v-model="filters.gender">
                      <label class="form-check-label" for="Femal">
                        Femal
                      </label>
                    </div>

                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseFour" aria-expanded="false" aria-controls="flush-collapseFour">
                    <i class="fa-solid fa fa-gear fw-bold mx-2"></i>
                    <span class="text-black">Entity</span>
                  </button>
                </h2>
                <div id="flush-collapseFour" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Hospital" id="Hospital" value="Hospital"
                        v-model="filters.entity">
                      <label class="form-check-label" for="Hospital">
                        Hospital
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Clinic" checked id="Clinic" value="Clinic"
                        v-model="filters.entity">
                      <label class="form-check-label" for="Clinic">
                        Clinic
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseFive" aria-expanded="false" aria-controls="flush-collapseFive">
                    <i class="pi pi-calculator fw-bold mx-2"></i>
                    <span class="text-black">Availability</span>
                  </button>
                </h2>
                <div id="flush-collapseFive" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="AnyDay" id="AnyDay" value="AnyDay"
                        v-model="filters.availability">
                      <label class="form-check-label" for="AnyDay">
                        AnyDay
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Today" checked id="Today" value="Today"
                        v-model="filters.availability">
                      <label class="form-check-label" for="Today">
                        Today
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Tomorrow" checked id="Tomorrow" value="Tomorrow"
                        v-model="filters.availability">
                      <label class="form-check-label" for="Tomorrow">
                        Tomorrow
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <!-- ////////Date//////////////// -->
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseDate" aria-expanded="false" aria-controls="flush-collapseDate">
                    <i class="pi pi-calendar fw-bold mx-2"></i>
                    <span class="text-black">Date</span>
                  </button>
                </h2>
                <div id="flush-collapseDate" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                      <div class="row">
                        <div class="col-md-6 col-xxl-6">
                          <div class="form-group">
                              <label class="form-label">From</label>
                              <Calendar v-model="filters.DateFrom" :placeholder="$t('13/3/2023')" :showIcon="true">
                              </Calendar>
                          </div>
                        </div>
                        <div class="col-md-6 col-xxl-6">
                          <div class="form-group">
                              <label class="form-label">To</label>
                              <Calendar v-model="filters.DateTo" :placeholder="$t('14/4/2024')" :showIcon="true">
                              </Calendar>
                          </div>
                        </div>
                      </div>
                  </div>
                </div>
              </div>
              <!-- //////////////////////////// -->
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseSex" aria-expanded="false" aria-controls="flush-collapseSex">
                    <i class="fa-solid fa fa-bomb fw-bold mx-2"></i>
                    <span class="text-black">Fees</span>
                  </button>
                </h2>
                <div id="flush-collapseSex" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="LE200" id="LE200" value="100__200"
                        v-model="filters.fees">
                      <label class="form-check-label" for="LE200">
                        100-200 L.E
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="LE400" checked id="LE400" value="200__400"
                        v-model="filters.fees">
                      <label class="form-check-label" for="LE400">
                        200-400 L.E
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseEight" aria-expanded="false" aria-controls="flush-collapseEight">
                    <i class="fa-solid fa fa-bullhorn fw-bold mx-2"></i>
                    <span class="text-black">Type</span>
                  </button>
                </h2>
                <div id="flush-collapseEight" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div v-for="option in optionsType"  :key="option.id" class="form-check mx-3">
                      <input class="form-check-input" type="checkbox"  :id="option.value" :value="option.value"
                        v-model="filters.type">
                      <label class="form-check-label" :for="option.value">
                      {{option.label}}
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseSeven" aria-expanded="false" aria-controls="flush-collapseSeven">
                    <i class="pi pi-tag fw-bold mx-2"></i>
                    <span class="text-black">Offers</span>
                  </button>
                </h2>
                <div id="flush-collapseSeven" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <h6> content from backend</h6>
                  </div>
                </div>
              </div>
            </div>
          </div>
          </Base>
        </div>
        <div class=" col-xxl-9 col-xl-12 col-lg-12 col-sm-12 col-md-12 my-5 ">
          <div class="search-clinics">
              <div class="row"> 
                <h4 class="mb-0">Search For Clinics</h4> 
              </div> 
              <Base>
                <div class="row">
                  <div class=" col-sm-12 col-md-4 col-xl-3 col-xxl-3">
                    <div class="p-inputgroup my-2">
                      <span class="p-inputgroup-addon bg-light">
                        <i class="pi pi-search"></i>
                      </span>
                      <AutoComplete v-model="clinics.searchName" :suggestions="drugNameParams.suggestions" field="value"
                        placeholder="Search by Name" @complete="search($event, drugNameParams)" />
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4 col-xl-3 col-xxl-3">
                    <div class="my-2">
                      <Dropdown v-model="clinics.selectSpeciality" :options="selectSpecialityOptions" optionLabel="value"
                        optionValue="value" placeholder="Select a Speciality " />
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4 col-xl-3 col-xxl-3">
                    <div class="my-2">
                      <Dropdown v-model="clinics.locationArea" :options="locationAreaOptions" optionLabel="value"
                        optionValue="value" placeholder="Location Area " />
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4 col-xl-3 col-xxl-3">
                    <div class="my-2">
                      <Dropdown v-model="clinics.insurance" :options="insuranceOptions" optionLabel="value"
                        optionValue="value" placeholder="Insurance " />
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4 col-xl-3 col-xxl-3">
                      <div class="d-flex my-2">
                        <div>
                          <button class="btn btn-success-gradient font-bold btn-pill mx-1 ">
                            <i class="pi pi-search mx-1"></i> Search </button>
                        </div>
                        <div  class="content-btn-filters">
                          <button  @click="displayFilters" class="btn btn-success-gradient font-bold btn-pill  m-x1 ">
                              <i class="pi pi-filter-fill mx-1" ></i> Filters </button>
                              <!-- <i class="pi" :class="[locale=='ar'?'pi-angle-double-left':'pi-angle-double-right']" ></i></button> -->
                        </div>
                      </div>
                  </div>
              
                </div>
              </Base>
          </div>
            <!-- //////////////Ophthalmology//////////v-if="saticDataLoadingTest" //////// -->
            <div class="content-ophthalmology">
              <!-- <div v-if="dummyData" class="content-ophthalmology "> -->
                <div class="row my-3 number-doctors">
                    <div class="fw-bold">
                        Ophthalmology
                        <span class="badge bg-secondary p-2 m-1 fw-bold">250 Doctors</span>
                    </div>
                    <div class="d-flex justify-content-start align-items-center" >
                        <div class="fw-bold">Ophthalmology</div>
                      <div><q class="text-secondary mx-4">250 Doctors</q></div>
                    </div>
                </div>
            
                <!-- <div class="row change-content mb-5" v-for="item in dummyData" :key='item.id'> -->
                <div class="row change-content content-num-doctors mb-5" >
                    <!-- <div class=""> -->
                      <div class="col-xl-7 col-lg-6 col-md-12 col-sm-12 p-0 m-0  animate__animated animate__fadeInDown ">
                        <!-- <div class=""> -->
                          <div class="profile-images position-relative ">
                              <div class="cover-pic ">
                                <!-- <img v-if="item.cover_image"  :src="item.cover_image" />  -->
                                <!-- <img  v-else :src="defaultImages.cover" /> -->
                                <img  :src="defaultImages.cover" />
                              </div>
                              <div class="custom-profile ">
                                <div class="avatar-container">
                                  <!-- <Avatar v-if="item.profile_image" :image="item.profile_image"   size="xlarge" class="ms-1" shape="circle"/> -->
                                  <!-- <Avatar v-else  :image="defaultImages.profile"   size="xlarge" class="ms-1" shape="circle"/> -->
                                  <Avatar  :image="defaultImages.profile"   size="xlarge" class="ms-1" shape="circle"/>
                                  <span class="badge-profile"></span>
                                  
                                </div>
                              
                              </div>
                              <!-- names[0].charAt(0) -->
                              <!-- <p>first==> firstLetter::{{item.name[0].charAt(0)}}</p>
                              <p>second==> firstLetter::{{item.name[1].charAt(0)}}</p> -->
                            
                              <div class="custom-icons d-flex justify-content-end align-items-center gap-2">
                                <div class="btn btn-circle bg-secondary">
                                  <!-- :href="item.social.faceboock" 
                                    :href="item.social.twitter"
                                    :href="item.social.linked_in"
                                  -->
                                  <a target="_blanck">
                                    <i class="fa fa-brands fa-facebook text-white"></i>
                                  </a>
                                </div>
                                <div class="btn btn-circle bg-secondary">
                                  <a  target="_blanck">
                                    <i class="fa fa-brands fa-twitter text-white" target="_blanck"></i>
                                  </a>
                                </div>
                                <div class="btn btn-circle bg-secondary">
                                  <a  target="_blanck">
                                    <i class="fa fa-brands fa-linkedin text-white"></i>
                                  </a>
                                </div>
                              </div>
                          </div>
                          <!-- ///////////////// -->
                          <div class="row custom-padding">
                            <div class="col-md-12">
                              <div class="d-flex  justify-content-between align-items-center flex-wrap">
                                <div class="name-doctors">
                                  <!-- <h6 class="mb-0">{{item.name}} </h6> -->
                                  <h6 class="mb-0">Dr.Mohamoud Hamed</h6>  
                                  <!-- <small class="text-success d-flex justify-content-center align-items-center"> {{item.title}}</small> -->
                                  <small class="text-success d-flex justify-content-center align-items-center px-1"> Consultant Of Ophthalmology</small>
                                </div>
                                <div class="content-overall-rating">
                                  <h6 class="mb-0">Overall rating:
                                    <span class="badge bg-success ">4/5</span>
                                  </h6>
                                  <Rating v-model="val2" :cancel="false" :readonly="true"/>
                                </div>
                                <div class="follow-message">
                                  <!-- mx-1  -->
                                  <button class="btn btn-secondary-gradient custom-width btn-pill">
                                    <i class="pi pi-book me-2"></i>Follow</button>
                                  <button class="btn btn-secondary-gradient custom-width btn-pill custom-margin-info">
                                    <i class="pi pi-send me-2"></i>Message</button>
                                </div>
                              </div>
                              <!-- ////////////////////////////////// -->
                              <div class="content">
                                <div class="row my-2">
                                  <!-- <div class="col-12"> -->
                                    <!-- <p class="border border-secondary "><q class="text-success"> {{item.description}}</q></p> -->
                                    <p class="border border-secondary "><q class="text-success">Health is a precious asst that we don't recognize and
                                      appreciate until it's depleted</q></p>
                                  <!-- </div> -->
                                </div>
                                <!-- ///////////////////////////// -->
                                <div class="row pb-2">
                                  <div class="col-xxl-6 col-md-6">
                                    <!-- /////////////Followers//////////// -->
                                    <div class="d-flex align-items-center justify-content-between flex-wrap " v-for="details in detailsOne" :key="details.id">
                                      <div class="content-icons-text">
                                        <i class="fa text-success " :class="details.icons"></i>
                                        <span class="fw-bold"> {{details.text}}</span>
                                      </div>
                                      <div class="content-value">
                                        <span class="fw-bold text-success">{{details.value}}</span>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="col-xxl-6  col-md-6 custom-border-info ">
                                    <!-- /////////////equipments/////////// -->
                                    <div class="d-flex align-items-center justify-content-between flex-wrap" v-for="details in detailsTwo " :key="details.id">
                                      <div class="content-icons-text">
                                        <i class="fa text-success" :class="details.icons"></i>
                                        <span class="fw-bold"> {{details.text}}</span>
                                      </div>
                                      <div class="content-value">
                                        <span class="fw-bold text-success">{{details.value}}</span>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      <!-- </div> -->
                      <!-- /////////////////////////////// -->
                      <div class=" col-xl-5 col-lg-6 col-md-12 col-sm-12  custom-border  animate__animated animate__fadeInDown">
                        <div class="custom-gray">
                          <CustomTabsNumbers v-model="selectedTab" :tabs="tabs" :checkError="check_error"
                            :serializerError="serializer_error" />  
                          </div>
                          <Divider></Divider>
                        <!-- /////////////Map///////////////// -->
                        <div v-show="selectedTab == 'Map'" class="content-map my-5">
                          <div class="svg-wrapper">
                            <img src="@/assets/search/Capture.svg" alt="" class="w-100">
                          </div>
                          <div class="d-flex justify-content-end align-items-center">
                            <div>
                              <button class="btn btn-secondary-gradient  btn-pill w-sm m-1 my-sm-0">
                                Get Direction
                              </button>
                            </div>

                          </div>
                        </div>
                        <!-- /////////////Booking/////////p-3/// -->
                        <div v-show="selectedTab == 'Booking'" class="content-booking  ">
                          <div v-if="bookingContent" class="content-bookin" >
                            <div v-if="toggleTypeDate"  class="row"> 
                              <div class="col-md-6 col-lg-12 col-xxl-6">
                                <div class="form-group">
                                  <label for="" class="form-label">Type</label>
                                  <Dropdown v-model="clinics.type" :options="typeOptions" optionLabel="value" optionValue="value"
                                    placeholder="Hospotal " />
                                </div>
                              </div>
                              <div class="col-md-6 col-lg-12  col-xxl-6">
                                <div class="form-group">
                                  <label class="form-label">Date</label>
                                  <Calendar v-model="selectedDate" :placeholder="$t('13/3/2023')" :showIcon="true">
                                  </Calendar>
                                  <!-- <div >{{ formattedDate}}</div> -->
                                  <!-- <Calendar v-model="clinics.date" :placeholder="$t('13/3/2023')" :showIcon="true"
                                    :class="{ 'p-invalid': $v.clinics.date.$error }" dateFormat="mm-dd-yy"
                                    @date-select="formateDate" />
                                  <small class="p-invalid" v-if="$v.clinics.date.$error && !$v.clinics.date.validDate">
                                    {{ dateError($t("Date")) }}
                                  </small> -->
                                </div>
                              </div>
                              <Divider></Divider>
                            </div>
                            <div class="contnt-toggle text-end">
                              <button @click="displayToggleTypeDate"  class="btn btn-outline-secondary"> <i class=" pi pi-angle-up"></i></button>
                            </div>
                            <!-- //////////////////// -->
                            <div class="setionBooking-view overflow-scroll " style="width: 100%; height:230px"  >
                              <div class="content-custom-carousel p-3">
                                <div v-for="booking in containsBooking" :key="booking.id">
                                    <div v-if="booking.day !== yesterday" class="d-flex justify-content-between align-items-center flex-wrap custom-shadow my-2 p-3">
                                      <div>
                                        
                                        <!-- <button v-if="todayDate == booking.day ? 'TODAY' : tomorrowDate == booking.day ? 'TOMORROW' : 'tomorrowDate == booking.day ? 'TOMORROW' '" class="btn btn-outline-secondary btn-pill"></button> -->
                                        <button v-if="todayDate == booking.day" class="btn btn-outline-secondary btn-pill">TODAY</button>
                                        <button v-else-if="tomorrowDate == booking.day" class="btn btn-outline-secondary btn-pill">TOMORROW</button>
                                        <div v-else>
                                          <div v-for="(date, index) in dateList"  :key="index"  >
                                            <button  v-if="date.format('dddd') == booking.day"   class="btn btn-outline-secondary btn-pill">
                                              {{  date.format('dd DD /MM') }}
                                            </button>
                                          </div>
                                        </div>
                                      </div>
                                    <div v-if="sections(booking).length > 0 " class="mx-1" >
                                      <div v-for="section in sections(booking)" :key="section.sectionNumber"  class="d-flex justify-content-between align-items-center flex-wrap gap-2">
                                        <div>  
                                          <!-- {{ section }} -->
                                          <span class="fw-bold">From</span>
                                          <span class=" fw-bold text-success">{{ section.openingTime }}</span>
                                        </div>
                                        <div>
                                          <span class="fw-bold ">To</span>
                                          <span class=" fw-bold text-success">{{ section.closingTime }}</span>
                                        </div>
                                      </div>
                                    </div>
                                      <!-- //////////disabled////////// -->
                                    <div v-else class="mx-1">
                                      <div  class="fw-bold">
                                          Not Available Appointments
                                      </div>
                                    </div>  

                                    <div v-if="sections(booking).length > 0" class="my-2">
                                      <button  @click="displayViewData" class="btn btn-secondary-gradient btn-pill">
                                        view
                                      </button>
                                    </div>
                                    <!-- :disabled="!(section.openingTime&&section.closingTime) " -->
                                      <div v-else class="my-2">
                                      <button class="btn btn-secondary-gradient btn-pill disabled">
                                        view
                                      </button>
                                      </div> 
                                    </div> 
                                </div>
                              </div>
                              <Divider></Divider>
                              <div class="content-carousel-booking"> 
                                <Carousel  :value="combinedAppointments" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions"  >	
                                    <template #item="slotProps">
                                        <div class="booking-item">
                                          <div class=" booking-item-content text-center ">
                                                <div class="px-3">
                                                  <button v-if="todayDate == slotProps.data.day" class="btn btn-outline-secondary btn-pill">TODAY</button>
                                                  <button v-else-if="tomorrowDate == slotProps.data.day" class="btn btn-outline-secondary btn-pill">TOMORROW</button>
                                                  <div v-else>
                                                    
                                                    <div v-for="(date, index) in dateList" :key="index">
                                                      <button v-if="date.format('dddd') == slotProps.data.day" class="btn btn-outline-secondary btn-pill">
                                                        {{ date.format('dd DD /MM') }}
                                                      </button>
                                                    </div>
                                                  </div>
                                                </div>
                                                <div v-if="slotProps.data.appointments.length >0" class="bookings" >
                                                  <div v-for="(appointment,index) in slotProps.data.appointments" :key="appointment.id" class="">
                                                    <!-- {{ slotProps.data }} -->
                                                    <table class="table table-borderless text-start">
                                                      <tbody>
                                                        <tr>
                                                          <td>From</td>
                                                          <td class="text-success">{{ appointment.appointmentFrom }}</td>
                                                        </tr>
                                                        <tr>
                                                          <td>To</td>
                                                          <td class="text-success">{{ appointment.appointmentTo  }}</td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <Divider v-if="slotProps.data.appointments.length > index+1"></Divider>
                                                  </div>
                                                </div> 
                                                <div v-else class="no-bookings ">
                                                  <div class="fw-bold mx-2">
                                                      Not Available Appointments
                                                  </div>
                                                </div>   
                                                <div  class="">
                                                  <button @click="displayViewContent(slotProps.data.day, slotProps.data.appointments)" class="btn btn-secondary-gradient btn-pill" :disabled="!slotProps.data.appointments.length >0">
                                                      view
                                                  </button> 
                                                </div>

                                              </div>
                                        </div>
                                      
                                    </template> 
                                </Carousel>

                              </div>
                            </div>
                          </div>    
                          <!-- ///////////displayView  TODAY,12/12/2023 -->
                        <!-- <div v-for="section in sectionsChoose(determineAppointment)" :key="section.sectionNumber"></div> -->

                          <div  v-if="displayView" class="show-view custom-shadow my-2 p-4">
                            <div class="table-responsive" >
                              <table class="table table-borderless text-nowrap mb-0 position-relative">
                                <!-- -->
                                <tbody class="">
                                  <div class="position-absolute custom-position"> 
                                    <img src="@/assets/search/imgBooking.svg"/>
                                  </div>
                                  <div class="mx-3 custom-cursor">
                                    <!-- <span>{{ determineAppointment.appointmentFrom }} - {{ determineAppointment.appointmentTo }}</span> -->
                                    <!-- <span class="d-none">{{ slotDurations}} </span> -->
                                  </div>
                                  <!-- {{ dividedOpeningTime() }} -->
                                    <!-- /////////////////////////// -->
                                    <div class="d-flex fw-bold text-success custom-margin">
                                      <div  class="mx-3 custom-cursor">
                                        <!-- <span></span> -->
                                      </div>
                                    </div>
                                  <tr>
                                    <td class="text-center"><span class="fw-bold">Choose Your appointment:</span> <span class="mx-2">{{ chooseDay }} </span></td>
                                  </tr>
                                  <tr>
                                    <td>
                                      <div class=" d-flex fw-bold text-success custom-margin">
                                        <div @click="openEditConfirm" class="mx-3 custom-cursor"><span> 02:30 pm</span></div> 
                                        <div class="mx-3 custom-cursor"> <span> 04:00 pm</span></div>
                                      </div> 
                                    </td>
                                  </tr>
                                  <tr><Divider></Divider></tr>
                                  <tr>
                                    <td >
                                      <div class=" d-flex fw-bold text-success custom-margin ">
                                        <div class="mx-3 custom-cursor"><span> 03:00 pm</span></div> 
                                        <div class="mx-3 custom-cursor"> <span> 03:30 pm</span></div>
                                        <div class="mx-3 custom-cursor"> <span> 04:30 pm</span></div>
                                        <div class="mx-3 custom-cursor"> <span> 06:00 pm</span></div>
                                        <div class="mx-3 custom-cursor"> <span> 6:30 pm</span></div>
                                      </div> 
                                    </td>
                                  </tr>
                                  <tr><Divider></Divider></tr>
                                  <tr>
                                    <td >
                                      <div class=" d-flex fw-bold text-success custom-margin">
                                        <div class="mx-3 custom-cursor"><span> 05:00 pm</span></div> 
                                        <div class="mx-3 custom-cursor"> <span> 05:30 pm</span></div>
                                      </div> 
                                      </td>
                                  </tr>

                                  <tr>
                                      <div class="d-flex justify-content-center align-items-center">
                                        <div><button @click="backBookingContent" class="btn btn-secondary-gradient btn-pill">Back</button></div>
                                      </div>
                                  </tr>
                                </tbody>
                              </table>
                            </div>
                          </div>
                          <!-- //////////////thanksBooking//////////// -->
                          <div v-if="thankAssistant" >
                              <div class="text-center custom-shadow  my-2 p-4">
                                <div class="fw-bold"> Thank You.</div>
                                <p class="fw-bold">
                                  Our assistant will notify you shortly.
                                </p>
                              </div>
                              <div class="d-flex justify-content-center align-items-center">
                                <div><button @click="hideThanks" class="btn btn-secondary-gradient btn-pill">Done</button></div>
                              </div>
                          </div>
                          <!-- ////////////confirm////////////////////// -->
                          <div class="confirm">
                            <ConfirmDialog 
                              :display="displayEditConfirm"
                              @no="closeEditConfirm"
                              @yes="saveConfirm"  
                            >
                              <div class="row">
                                <div class="col-md-12  ">
                                  <div class="">
                                        <h5 class="fw-bold text-success"> Are You Sure you want to confirm 
                                          <q>
                                            <span class="fw-bold text-black">Today, 12/12/2023, 6:00 PM </span>
                                          </q> 
                                        <br/> as your appointment?
                                        </h5> 
                                  </div>                 
                                </div>
                              </div>
                            </ConfirmDialog>
                          </div>
                          <!-- /////////////steps/////////////// -->
                          <div class="booking w-100">
                              <router-view></router-view>
                              <Steps :model="steps" :readonly="false" class="my-3" />
                          </div>
                        </div>
                        <!-- /////////////Photos///////p-3/ -->
                        <div v-show="selectedTab == 'Photos'" class="content-photo  my-5">
                          <!-- <div v-if="item.photos">
                            <div  class="content-galleria">
                              <Galleria :value="item.photos" :activeIndex.sync="activeIndex" :responsiveOptions="responsiveOptions" :numVisible="7" containerStyle="width: 550px"
                                :circular="true" :fullScreen="true" :showItemNavigators="true" :showThumbnails="false" :visible.sync="displayCustom">
                                <template #item="slotProps">
                                  <img :src="slotProps.item.src" :alt="slotProps.item.alt" style="width:100%;display: block; " />
                                </template>
                                <template #thumbnail="slotProps">
                                  <img :src="slotProps.item.src" :alt="slotProps.item.alt" style="display: block;" /> 
                                </template>
                              </Galleria>
                            </div>
                    
                            <div v-if="item.photos" class="row" >
                              <div v-for="(image, index) of item.photos" class="col-xxl-3 col-6 my-2" :key="index"  >
                                  <div  v-if="index < 3" class="w-100 h-100">
                                  <img :src="image.src" :alt="image.alt" style="cursor: pointer" class="w-100 h-100" @click="imageClick(index)"/>
                                  </div>
                                  <div v-if="hideImage && index == 3" class="w-100 h-100 position-relative "  @click="imageExtended()" >
                                    <img :src="image.src" :alt="image.alt"  class="w-100 h-100" style="cursor: pointer"/>
                                    <div class="custom-overlay"></div>
                                    <div class="custom-number">+3</div>
                                  </div>
                                  <div v-show="extendImage" v-if="index >= 3"  class="w-100 h-100">
                                    <img :src="image.src" :alt="image.alt"  class="w-100 h-100" style="cursor: pointer" @click="imageClick(index)"/>
                                  </div>

                              </div>
                            </div>
                          </div> -->
                            <!-- ///////////////////// -->
                          <div class="overflow-scroll p-3" style="width: 100%; height: 200px">
                            <div class="content-galleria">
                              <!-- width: 550px -->
                              <Galleria :value="defaultImages.images" :activeIndex.sync="activeIndex" :responsiveOptions="responsiveOptions" :numVisible="7" containerStyle="width: 50% "
                                :circular="true" :fullScreen="true" :showItemNavigators="true" :showThumbnails="false" :visible.sync="displayCustom">
                                <template #item="slotProps">
                                  <img :src="slotProps.item.src" :alt="slotProps.item.alt" style="width:100%;display: block; " />
                                </template>
                                <template #thumbnail="slotProps">
                                  <img :src="slotProps.item.src" :alt="slotProps.item.alt" style="display: block;" />
                                  
                                </template>
                              </Galleria>
                            </div>
                            <div v-if="defaultImages.images" class="row" >
                              <div v-for="(image, index) of defaultImages.images" class="col-xxl-3 col-6 my-2" :key="index"  >
                                  <div  v-if="index < 3" class="w-100 h-100">
                                  <img :src="image.src" :alt="image.alt" style="cursor: pointer" class="w-100 h-100" @click="imageClick(index)"/>
                                  </div>
                                  <div v-if="hideImage && index == 3" class="w-100 h-100 position-relative "  @click="imageExtended()" >
                                    <img :src="image.src" :alt="image.alt"  class="w-100 h-100" style="cursor: pointer"/>
                                    <div class="custom-overlay"></div>
                                    <div class="custom-number">+3</div>
                                  </div>
                                  <div v-show="extendImage" v-if="index >= 3"  class="w-100 h-100">
                                    <img :src="image.src" :alt="image.alt"  class="w-100 h-100" style="cursor: pointer" @click="imageClick(index)"/>
                                  </div>
                              </div>
                            </div>
                          </div>

                        </div>
                        <!-- ////////////Rating//////////p-3 /// -->
                        <div v-show="selectedTab == 'Ratings'" class="content-rating my-5 ">
                          <div class="row ">
                            <div class="col-12">
                              <div class="d-flex align-items-center justify-content-start">
                                <label class="form-label ">Your rating:</label> 
                                <div class="form-label mx-2">
                                  <div class="p-rating">
                                      <Rating v-model="valRatings" :cancel="false" class="custom-rating " />
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="col-md-2 col-lg-12">
                              <div class=""> <label class="form-label ">AddComment:</label> </div>
                            </div>
                            <div class="col-md-7 col-lg-12 ">
                              <div class="">
                                <input type="text" placeholder="Type..." v-model="clinics.comment" class="form-control">
                              </div>  
                            </div>
                            <div  class="col-md-3 col-lg-12 my-lg-2" v-if="showComment">
                              <div class="">
                                <button class="btn btn-secondary-gradient btn-pill">Comment</button>
                              </div>
                            </div>
                          </div>
                          <!-- /////////////scroll Rating////////// -->
                          <div  class="overflow-scroll p-3" style="width: 100%; height: 240px">
                            <div class="row custom-shadow  p-3 my-2" v-for="comment in containscommentRating" :key="comment.id">
                              <!-- <div class="col-md-12  ">
                                <div class="d-flex align-items-center justify-content-start p-2">
                                <div id="triangle-right"><span class="position-absolute  rating-text-span">{{comment.rate}}</span></div>
                                  <div class="p-rating bg-success custom-radius  ">
                                  
                                    <Rating severity="warning" v-model="commentRatings"  :readonly="true" :cancel="false"  :stars="5" />
                                  </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-start ">
                                  <div class="avatar-container">
                                  <Avatar :image="defaultImages.profile"  class="ms-1" shape="circle"/>
                                  <span class="badge-profile-rating"></span>
                                </div>
                                  <span class="fw-bold mx-1 ">{{comment.name}}</span>

                                </div>
                                <small class="mx-4 text-wrap custom-small"> {{comment.date}}</small>
                                <p class="mx-2"><q> {{comment.clinic}}</q></p>
                                <div class="d-flex align-items-center justify-content-between flex-wrap">
                                  <div class="my-1 ">
                                    <button class="btn btn-pill btn-outline-success custom-width"><i class=" fa fa-solid fa-thumbs-up"></i> {{comment.agree}}</button>
                                  </div>
                                  <div class="my-1">
                                    <button class="btn btn-pill btn-outline-danger custom-width "><i class="  fa fa-regular fa-thumbs-down"></i> {{comment.disagree}}</button>
                                  </div>
                                </div>
                              </div> -->
                              <div class="col-md-6 col-lg-12 order-lg-2 ">
                                  <div class="d-flex align-items-center justify-content-start p-2">
                                  <div id="triangle-right"><span class="position-absolute  rating-text-span">{{comment.rate}}</span></div>
                                    <div class="p-rating bg-success custom-radius  ">
                                    
                                      <Rating severity="warning" v-model="commentRatings"  :readonly="true" :cancel="false"  :stars="5" />
                                    </div>
                                  </div>
                                  <div class="d-flex align-items-center justify-content-start flex-wrap gap-2">
                                  <div class="">
                                    <button class="btn btn-pill btn-outline-success custom-width-rating "><i class=" fa fa-solid fa-thumbs-up"></i> {{comment.agree}}</button>
                                  </div>
                                  <div class="">
                                    <button class="btn btn-pill btn-outline-danger custom-width-rating  "><i class="  fa fa-regular fa-thumbs-down"></i> {{comment.disagree}}</button>
                                  </div>
                                  </div>
                              </div>
                              <div class="col-md-6 col-lg-12 order-lg-1"> 
                                  <div class="d-flex align-items-center justify-content-start ">
                                    <div class="avatar-container">
                                    <Avatar :image="defaultImages.profile"  class="ms-1" shape="circle"/>
                                    <span class="badge-profile-rating"></span>
                                  </div>
                                    <span class="fw-bold mx-1 ">{{comment.name}}</span>

                                  </div>
                                  <small class="mx-4 text-wrap custom-small"> {{comment.date}}</small>
                                  <p class="mx-2"><q> {{comment.clinic}}</q></p>
                              </div>
                              <!-- <div class="col-md-6 ">
                                <div class="d-flex align-items-center justify-content-between flex-wrap">
                                  <div class="my-1 ">
                                    <button class="btn btn-pill btn-outline-success custom-width"><i class=" fa fa-solid fa-thumbs-up"></i> {{comment.agree}}</button>
                                  </div>
                                  <div class="my-1">
                                    <button class="btn btn-pill btn-outline-danger custom-width "><i class="  fa fa-regular fa-thumbs-down"></i> {{comment.disagree}}</button>
                                  </div>
                                </div>
                              </div> -->
                              </div>
                            </div>
                          <!-- </div>    -->
                        </div>
                      </div>
                    <!-- </div> -->
                </div>

              </div>
              <!--  v-if="!dummyData -->
              <div v-if="dummyDataWorkTest" class="d-flex justify-content-center align-items-center">
                <div class=""><img :src="defaultImages.search"/> <h4 class="text-center">Search for Clinic...</h4></div>
              </div>
        </div>
        <!-- /////////////////Filters////////////// -->
        <div  class="col-xxl-3  custom-height custom-filters-large-screen ">
          <Base>
          <div class="content-filters">
            <h5 class="text-center mb-0"> FILTERS </h5>
            <Divider class="m-0"></Divider>
            <div class="accordion accordion-flush background-body" id="accordionFlushExample">
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                    <i class="pi pi-paypal  mx-2"></i>
                    <span class="text-black">Title</span>
                  </button>
                </h2>
                <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Professor" id="Professor" value="Professor"
                        v-model="filters.title">
                      <label class="form-check-label" for="Professor">
                        Professor
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Specialist" checked id="Specialist"
                        value="Specialist" v-model="filters.title">
                      <label class="form-check-label" for="Specialist">
                        Specialist
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                    <i class="fa-solid fa fa-stethoscope fw-bold mx-2"></i><span class="text-black">Sub Specialities</span>
                  </button>
                </h2>
                <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Dentistry" id="Dentistry" value="Dentistry"
                        v-model="filters.specialities">
                      <label class="form-check-label" for="Dentistry">
                        Dentistry
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Dermatology" checked id="Dermatology"
                        value="Dermatology" v-model="filters.specialities">
                      <label class="form-check-label" for="Dermatology">
                        Dermatology
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                    <i class="fa-solid fa fa-venus-mars fw-bold mx-2"></i>
                    <span class="text-black">Gender</span>
                  </button>
                </h2>
                <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Male" id="Male" value="Male"
                        v-model="filters.gender">
                      <label class="form-check-label" for="Male">
                        Male
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Femal" checked id="Femal" value="Femal"
                        v-model="filters.gender">
                      <label class="form-check-label" for="Femal">
                        Femal
                      </label>
                    </div>

                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseFour" aria-expanded="false" aria-controls="flush-collapseFour">
                    <i class="fa-solid fa fa-gear fw-bold mx-2"></i>
                    <span class="text-black">Entity</span>
                  </button>
                </h2>
                <div id="flush-collapseFour" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Hospital" id="Hospital" value="Hospital"
                        v-model="filters.entity">
                      <label class="form-check-label" for="Hospital">
                        Hospital
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Clinic" checked id="Clinic" value="Clinic"
                        v-model="filters.entity">
                      <label class="form-check-label" for="Clinic">
                        Clinic
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseFive" aria-expanded="false" aria-controls="flush-collapseFive">
                    <i class="pi pi-calculator fw-bold mx-2"></i>
                    <span class="text-black">Availability</span>
                  </button>
                </h2>
                <div id="flush-collapseFive" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="AnyDay" id="AnyDay" value="AnyDay"
                        v-model="filters.availability">
                      <label class="form-check-label" for="AnyDay">
                        AnyDay
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Today" checked id="Today" value="Today"
                        v-model="filters.availability">
                      <label class="form-check-label" for="Today">
                        Today
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="Tomorrow" checked id="Tomorrow" value="Tomorrow"
                        v-model="filters.availability">
                      <label class="form-check-label" for="Tomorrow">
                        Tomorrow
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <!-- ////////Date//////////////// -->
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseDate" aria-expanded="false" aria-controls="flush-collapseDate">
                    <i class="pi pi-calendar fw-bold mx-2"></i>
                    <span class="text-black">Date</span>
                  </button>
                </h2>
                <div id="flush-collapseDate" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                      <div class="row">
                        <div class="col-xl-12 col-xxl-6">
                          <div class="form-group">
                              <label class="form-label">From</label>
                              <Calendar v-model="filters.DateFrom" :placeholder="$t('13/3/2023')" :showIcon="true">
                              </Calendar>
                          </div>
                        </div>
                        <div class="col-xl-12 col-xxl-6">
                          <div class="form-group">
                              <label class="form-label">To</label>
                              <Calendar v-model="filters.DateTo" :placeholder="$t('14/4/2024')" :showIcon="true">
                              </Calendar>
                          </div>
                        </div>
                      </div>
                  </div>
                </div>
              </div>
              <!-- //////////////////////////// -->
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseSex" aria-expanded="false" aria-controls="flush-collapseSex">
                    <i class="fa-solid fa fa-bomb fw-bold mx-2"></i>
                    <span class="text-black">Fees</span>
                  </button>
                </h2>
                <div id="flush-collapseSex" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="LE200" id="LE200" value="100__200"
                        v-model="filters.fees">
                      <label class="form-check-label" for="LE200">
                        100-200 L.E
                      </label>
                    </div>
                    <div class="form-check mx-3">
                      <input class="form-check-input" type="radio" name="LE400" checked id="LE400" value="200__400"
                        v-model="filters.fees">
                      <label class="form-check-label" for="LE400">
                        200-400 L.E
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseEight" aria-expanded="false" aria-controls="flush-collapseEight">
                    <i class="fa-solid fa fa-bullhorn fw-bold mx-2"></i>
                    <span class="text-black">Type</span>
                  </button>
                </h2>
                <div id="flush-collapseEight" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <div v-for="option in optionsType"  :key="option.id" class="form-check mx-3">
                      <input class="form-check-input" type="checkbox"  :id="option.value" :value="option.value"
                        v-model="filters.type">
                      <label class="form-check-label" :for="option.value">
                      {{option.label}}
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion-item background-body">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed  fw-bold  text-success" type="button" data-bs-toggle="collapse"
                    data-bs-target="#flush-collapseSeven" aria-expanded="false" aria-controls="flush-collapseSeven">
                    <i class="pi pi-tag fw-bold mx-2"></i>
                    <span class="text-black">Offers</span>
                  </button>
                </h2>
                <div id="flush-collapseSeven" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <h6> content from backend</h6>
                  </div>
                </div>
              </div>
            </div>
          </div>
          </Base>
        </div>
      </div>
    </div>
  </div>
</template>
<i18n  lang="json5">
  {
    "en":{
      "booking":"Booking", 
      "appointment":"Appointment",
      "thank":"Thank"
    },
    "ar":{ 
      "booking":"Booking", 
      "appointment":"Appointment",
      "thank":"Thank"
    }
  }
</i18n>
<script>
import Base from "@/components/global/utilities/Base.vue";
import Divider from "@/components/global/utilities/Divider.vue";
import CustomTabsNumbers from "@/components/labs/lab/custom/CustomTabsNumbers.vue";
import { validDate } from "@/validation/customValidators";
// ////////////////////////////////////////////////////////
import { convertDate } from "@/helpers/utilities";
import { dateError } from "@/validation/errors";
///////////////////////
import searchClinicsOptions from "@/mixins/searchClinics/searchClinicsOptions";
import ConfirmDialog  from "@/components/global/utilities/ConfirmDialog .vue"
//////////////////////////////
import moment from 'moment';
///////////////////////////////////
import {cloneDeep} from 'lodash';
import axios from 'axios'
export default {
  name: "searchClinicsCore",
  mixins:[searchClinicsOptions],
  components: {
    Base,
    Divider,
    CustomTabsNumbers,
    ConfirmDialog ,
  },
  data() {
    return {
      //////////////////////
      dummyData:null,
      dummyDataWorkTest:false,
      //////////////////
      // openingTime: "03:30 PM", // Opening time
      // closingTime: "06:30 PM", // Closing time
      sectionDuration: 30, // Duration of each section in minutes
      /////////////////
      selectedDate: null,
      selectedDateText: '',
      /////////////////
      // true or false
      saticDataLoadingTest:true,
      hideFilterScreen:false,
      /////////////////////
      val2: 4,
      valRatings: 2,
      commentRatings: 3,
      hideFilter: true,
      displayView:false,
      bookingContent:true,
      showComment:false,
      ///////////////////////
      visibleRight: false,
      ////////////////////
      extendImage:false,
      hideImage:true,
      /////////////////////
      displayEditConfirm:false,
      thankAssistant:false,
      //////////////////////
      activeIndex: 0,
      displayCustom: false,
      //////////////////////
      reports: null,
      ////////////////////////////
      defaultImages: {
        // profile: require("@/assets/search/profile.svg"),
        // cover: require("@/assets/search/cover.svg"),
        // cover: require("@/assets/search/1.jpg"),
        profile: require("@/assets/search/2.jpg"),
        cover: require("@/assets/search/images.jpg"),
        ///////////////////////////////////////////
        search: require("@/assets/search/search.svg"),
        images: [
          { id: 1, src: require("@/assets/search/slider_1.svg"), alt: "Image from 1" },
          { id: 2, src: require("@/assets/search/slider_2.svg"), alt: "Image 2" },
          { id: 3, src: require("@/assets/search/slider_3.svg"), alt: "Image 3" },
          { id: 4, src: require("@/assets/search/slider_4.svg"), alt: "Image 4" },
          { id: 5, src: require("@/assets/search/slider_2.svg"), alt: "Image 5" },
          { id: 6, src: require("@/assets/search/slider_4.svg"), alt: "Image 6" },
          { id: 7, src: require("@/assets/search/slider_1.svg"), alt: "Image 7" },
          { id: 8, src: require("@/assets/search/slider_3.svg"), alt: "Image 8" },
          { id: 9, src: require("@/assets/search/slider_4.svg"), alt: "Image 9" },
          { id: 10, src: require("@/assets/search/slider_1.svg"), alt: "Image 10" },

        ],
      },
      ////////////////////
      center: { 
        lat: 30.0444,
        lng: 31.2357
      },
      //////////Backend////////////  
      containscommentRating:[],
      containsBooking:[
        {day:'Friday',},
        {day:'Saturday', appointmentFrom:'03:00 AM',appointmentTo:'04:00 AM '},
        {day:'Sunday', appointmentFrom:'5:30 AM',appointmentTo:'06:30 AM'},
        {day:'Monday',  appointmentFrom:'04:00 AM',appointmentTo:'04:30 AM '},
        {day:'Tuesday', appointmentFrom:'04:30 AM',appointmentTo:'05:00 AM '},
        {day:'Tuesday', appointmentFrom:'08:30 AM',appointmentTo:'10:00 AM '},
        {day:'Wednesday',appointmentFrom:'04:00 AM',appointmentTo:'06:30 AM ' },
        {day:'Thursday', appointmentFrom:'03:00 PM',appointmentTo:'06:00 PM ' },
      ],
      detailsOne:[
        {icons:'fa-users',text:'Followers',value:1.269},
        {icons:'fa-stethoscope',text:'Specializable in',value:'Aduilt Ophthalmology'},
        {icons:'fa-money',text:'Fees',value:'500 LE'},
        {icons:'fa-file',text:'Insurance',value:'AXA, Metlife'},
       
      ],
      detailsTwo:[
        {icons:'fa-users',text:'Equipment',value:'Sonar'},
        {icons:'fa-building',text:'Location',value:'Nasr City'},
        {icons:'fa-euro',text:'Waiting Time',value:'45 min'},
        {icons:'fa-phone',text:'Contacts',value:'01200000000'},
       
      ],
      ////////////////////////////
      yesterday :null,
      todayDate:null,
      tomorrowDate:null,
      anyDate:null,
      ///////////////////
      combinedAppointments:[],
      responsiveOptions: [
          // {
          //     breakpoint: '1440px',
          //     numVisible: 3,
          //     numScroll: 1
          // },
          {
              breakpoint: '1024px',
              numVisible: 3,
              numScroll: 1
          },
          {
              breakpoint: '600px',
              numVisible: 2,
              numScroll: 1
          },
          {
              breakpoint: '480px',
              numVisible: 1,
              numScroll: 1
          }
      ],
    //////////////////////////
     // Initialize with today's date
      startDate: moment(),
      dateList: [],
      ///////////////////////
      //  name: null,
      //  speciality:{
      //   id:null
      //  },
      ///////////////////////
      chooseDay:"",
      chooseAppointments:[],
      dividedOpeningTime:[],
      toggleTypeDate:false,
      clinics: {
        searchName: null,
        selectSpeciality: null,
        locationArea: null,
        insurance: null,
        type: null,
        date: null,
        comment: "",
      },
      filters: {
        title: "",
        specialities: "",
        gender: "",
        entity: "",
        availability: "",
        DateFrom: "",
        DateTo: "",
        fees: "",
        type:[],
      },
      check_error: {},
      serializer_error: {},
      // Map
      selectedTab: "Map",
      tabs: [
        { en: "Booking", ar: "Booking", key: "Booking" },
        { en: "Map", ar: "Map", key: "Map" },
        { en: "Photos", ar: "Photos ", key: "Photos" },
        { en: "Ratings", ar: "Ratings", key: "Ratings" },
      ],
      //////////////////////
      optionsType: [
        { label: 'Clinic', value: 'clinic' },
        { label: 'Hosiptal', value: 'hosiptal' },
        { label: 'Video Call', value: 'VideoCall' },
        { label: 'Visit at Home', value: 'VisitHome' },
      ],
      selectedOptions: [],
    };
  },
  created() {
    let commentNumber= 3;
    for(let comment=0; comment<=commentNumber; comment++){
      this.containscommentRating.push(this.comments());
    }
    ////////////////////
    this.todayDate = moment().format('dddd');
    this.anyDate =  moment().add(2, 'day').format('dddd');
    this.tomorrowDate = moment().add(1, 'day').format('dddd');
    this.yesterday = moment().subtract(1, 'day').format('dddd');
    ////////////////////////////
    this.generateDates();
    ///////////////////
    this.contentSumAppointment();
    /////////////////////////

  },
  mounted() {
    // this.fetchStaticData();
    this.testDummyStaticData();
    this.orderBookingListScroll();
    this.orderBookingList();
    ///////////////////////////
    this.slotDurations;
  //  this.dividedOpeningTime =cloneDeep(this.slotDurations) ;
    
  },
  watch: {
  'clinics.comment':{
    deep: true,
    handler(newValue,oldValue){
      console.log("oldValue"+ oldValue);
      if(newValue != ""){
        this.showComment= true;
      }
      else return this.showComment= false;
   }
  }

  },
  /////////////////////
  computed: {
    steps(){
      return [
        {
          to: "#booking",
          label: this.$t('booking'),
        },
        {
          to:"#appointment",
          label: this.$t('appointment'),
        },
        {
          to:"#thank",
          label: this.$t('thank'),
        }
      ];  
    },
    ////////////////////////////
    slotDurations() {
      return this.chooseAppointments.map(appointment => {
      const opening = moment(appointment.appointmentFrom, 'hh:mm a');
      const closing = moment(appointment.appointmentTo, 'hh:mm a');
      // console.log("opening from slotduration use moment.js" + opening);
      // console.log("closing from slotduration use moment.js" + closing);
      /////////////////////////
      const sectionDuration = this.sectionDuration;
      /////////////////////////////////////////////
      // console.log("sectionDuration" + sectionDuration)
      const diffInMinutes = closing.diff(opening, "minutes");
      // console.log("diffInMinutes" + diffInMinutes)
      const numberOfSections = Math.floor(diffInMinutes / sectionDuration);
      // console.log("numberOfSections" + numberOfSections)
      let startTime = opening.clone();
      console.log("opening" + startTime)
      for (let i = 0; i < numberOfSections; i++) {
        const endTime = startTime.clone().add(sectionDuration, "minutes");
          this.dividedOpeningTime.push({
          sectionNumber: i + 1,
          openingTime: startTime.format("hh:mm A"),
          closingTime: endTime.format("hh:mm A"),
        });
        startTime = endTime;
      }
      // });
      return this.dividedOpeningTime;
    });
    },
    ////////////////////////////////////
    sections() {
      return (booking) =>{
        //////////////////////////////////
        const sections = [];
        const now = moment();
        const currentTimestamp = now.valueOf(); 
        // console.log("currentTimestamp"+currentTimestamp)
        // console.log("time now from Randa " + now);
        // console.log("time appointmentFrom from Randa " + booking.appointmentFrom);
        const openingTime = moment(booking.appointmentFrom, "hh:mm A");
        const lets = now.isSameOrAfter(openingTime);
        // console.log("lets::==> " + lets);
        if(lets) {
            // console.log("openingTime Randa" + openingTime);
            const closingTime = moment(booking.appointmentTo, "hh:mm A");
            // console.log("closingTime Randa Ali" +closingTime)
            const sectionDuration = this.sectionDuration;
            const diffInMinutes = closingTime.diff(openingTime, "minutes");
            const numberOfSections = Math.floor(diffInMinutes / sectionDuration);
            let startTime = openingTime.clone();
            for (let i = 0; i < numberOfSections; i++) {
              const endTime = startTime.clone().add(sectionDuration, "minutes");
              sections.push({
                sectionNumber: i + 1,
                openingTime: startTime.format("hh:mm A"),
                closingTime: endTime.format("hh:mm A"),
              });
              startTime = endTime;
            }
          return sections;
        }
        else{
          return  sections;
        }  
      }
    },
    ////////////////////////
    formattedDate() {
      if (this.selectedDate) {
          const selected = moment(this.selectedDate);
          const today = moment().startOf('day');
          const tomorrow = moment().add(1, 'day').startOf('day');
          if (selected.isSame(today, 'day')) {
            return 'Today';
          } else if (selected.isSame(tomorrow, 'day')) {
            return 'Tomorrow';
          } else {
            return selected.format('dd  DD / MM');
          }
      }
     return '';
    }, 
  },
  ////////////////////////
  methods: {
    contentSumAppointment() {
      const array1 = [
        { day: 'Friday' },
        { day: 'Saturday', appointmentFrom: '03:00 AM', appointmentTo: '04:00 AM' },
        { day: 'Sunday', appointmentFrom: '5:30 pm', appointmentTo: '06:30 pm' },
        { day: 'Monday', appointmentFrom: '10:00 AM', appointmentTo: '04:30 AM' },
        { day: 'Monday', appointmentFrom: '08:00 AM', appointmentTo: '04:30 AM' },
        { day: 'Tuesday', appointmentFrom: '04:30 AM', appointmentTo: '05:00 AM' },
        { day: 'Tuesday', appointmentFrom: '04:30 AM', appointmentTo: '05:00 AM' },
        { day: 'Wednesday', appointmentFrom: '04:00 AM', appointmentTo: '06:30 AM' },
        { day: 'Wednesday', appointmentFrom: '09:00 AM', appointmentTo: '12:30 AM' },
        { day: 'Thursday', appointmentFrom: '03:00 PM', appointmentTo: '06:00 PM' },
        { day: 'Thursday', appointmentFrom: '08:00 PM', appointmentTo: '12:00 PM' },
      ];

      this.combinedAppointments = [];
      array1.forEach(appointment => {
        const day = appointment.day;
        if (!this.combinedAppointments.find(item => item.day === day)) {
          this.combinedAppointments.push({
            day: day,
            appointments: [],
          });
          
        }
        if (appointment.appointmentFrom && appointment.appointmentTo) {
          this.combinedAppointments.find(item => item.day === day).appointments.push({
            appointmentFrom: appointment.appointmentFrom,
            appointmentTo: appointment.appointmentTo,
          });
        }
      });

      return this.combinedAppointments;
    },
    //////////////////////////////
    orderBookingList() {
      const today = moment().format('dddd');
      ////////// combinedAppointments//////////
      // console.log("orderBookingList from today:: ==>> " + today)
      // console.log("orderBookingList from combinedAppointments"+this.combinedAppointments)
      const todayIndex = this.combinedAppointments.findIndex(booking => booking.day === today);
      // console.log("todayIndex==> " + todayIndex)
      if (todayIndex === -1) {
        // console.error('Today is not found in containsBooking.');
        return;
      }
      // Reorder the containsBooking array starting from today
      const orderedList = [
        ...this.combinedAppointments.slice(todayIndex),
        ...this.combinedAppointments.slice(0, todayIndex),
      ];
      // console.log("orderedList from randa" + orderedList);
        this.combinedAppointments = orderedList;

    },
    //////////////////////////////////////////
    dateError,
    //////////////////////
    orderBookingListScroll() {
      const today = moment().format('dddd');
      const todayIndex = this.containsBooking.findIndex(booking => booking.day === today);
      // console.log("todayIndex==> " + todayIndex)
      if (todayIndex === -1) {
        // console.error('Today is not found in containsBooking.');
        return;
      }
      // Reorder the containsBooking array starting from today
      const orderedList = [
        ...this.containsBooking.slice(todayIndex),
        ...this.containsBooking.slice(0, todayIndex),
      ];
      console.log("containsBooking"+ orderedList)
      this.containsBooking = orderedList;
    },
    //////////////////////////////
    generateDates() {
      this.dateList = [];
      for (let i = 0; i < 7; i++) { 
        // Generate dates for 5 weeks (you can adjust as needed).format('dddd')
        this.dateList.push(moment(this.startDate).add(i , 'days'));
      }
    },
    //////////////////////
    imageExtended(){
      this.extendImage =!this.extendImage;
      this.hideImage =false;
    },
    /////////////////////////
    displayToggleTypeDate(){
      this.toggleTypeDate =!this.toggleTypeDate;
    },
    ////////////////////////
    displayViewData(){
      this.displayView = true;
      this.bookingContent = false;
    },
    //////////////////////////
    displayViewContent(daySelect,appointment){
      // console.log("from daySelect",daySelect)
      this.dateList.map(originalDate => {
        const day = moment(originalDate).format('dddd');
          const formattedDate = moment(originalDate).format('DD/MM/YYYY'); // Adjust the format as needed
            if(day === daySelect ) {
              this.chooseDay = `${daySelect}, ${formattedDate}`;
              this.chooseAppointments = appointment;
              // console.log("appointment",appointment)
              this.displayView = true;
              this.bookingContent = false;
            }
        }
      );
    },
    //////////////Confirm///////////////
    openEditConfirm(){
      this.displayEditConfirm = true;
    },
    closeEditConfirm() {
     this.displayEditConfirm = false;
    },
    saveConfirm() {
     this.displayEditConfirm = false;
     this.displayView = false;
     this.bookingContent = false;
     this.thankAssistant = true;
    },
    hideThanks(){
      this.thankAssistant = false;
      this.bookingContent = true;
    },
    backBookingContent(){
      this.bookingContent = true;
      this.displayView = false;
    },
    /////////Data from Backend/////////////
    comments(){
        return{
          img:"",
          name:'Magday Afsha',
          date:'Mon, 8/10/2022, 3:30 PM ',
          rate:'4.0',
          clinic:'His clinics is well prepared , expert in his job and also polite as a man',
          agree:'Agree',
          disagree:'Disagree',   
        }
    },
    /////////////googleMap////////////////
    getLocation(event){
      this.center = {
          lat: event.latLng.lat(),
          lng: event.latLng.lng()
      };
      // console.log(this.center);
      this.form.location.coordinates.lg = this.center.lng ;
      this.form.location.coordinates.lt = this.center.lat ;
    },
    /////////////////
    displayFilters() {
      this.hideFilter = !this.hideFilter;
      this.hideFilterScreen = ! this.hideFilterScreen
    },
    closeFilersScreen(){
      this.hideFilterScreen =false;
    },
    ////////////////
    formateDate() {
      this.clinics.date = convertDate(this.clinics.date);
    },
    ////////////////////////
    imageClick(index) {
      this.activeIndex = index;
      this.displayCustom = true;
    },
    ////////////test dummy static data////////////////
     async testDummyStaticData(){
      await axios.get("https://my.api.mockaroo.com/search_clinics.json?key=c45d22e0")
      .then((response)=>{
        //  this.dummyData =(...response.data);
         this.dummyData = cloneDeep(response.data);
         console.log(this.dummyData)
      })
      .catch((error)=>{
        console.log(error)
      })

     }

    /////////////////////////////////////////////////
    // async fetchStaticData() { 
    //   try {
    //     const response = await axios.get('/path/to/static/data.json');
    //     console.log(response.data);
    //     return response.data;
    //   } catch (error) {
    //     console.log(error);
    //     console.error('Error fetching data: Eng:Randa Ali', error);
    //     throw error;
    //   }

    // //  this.$store.dispatch('clinicsStaticData/loadStaticData')
    // //  .then((res) => {
    // //    console.log(res);
    // //    this.check_error = {};
    // //    this.serializer_error = {};
    // //   })
        
    //   },
  },
  validations: {
    clinics: {
      date: {
        validDate(value) {
          return validDate(value);
        },
      },
    },
  },
};
</script>
<style scoped lang="scss" >
.content-scroll{
//     width: 100%;
    // height: 200px;
    // overflow-y: auto;
  // background-color: #333;
  // position: fixed;
  // left: 0;
  // top: 0;
  // right: 0;
  // width: 100%;
  // height: 100%;
  // min-height: 100px;
  // overflow: scroll;
}
.content-core{
  // background-color: red;
  // height: 50vw;
  // width: 100vw;
  

}
.custom-width{
  min-width:125px;
  
}
.custom-width-rating{
  min-width:95px;
  padding: 2px;
  
}
.content-carousel-booking{
 width:100%;
}
.custom-filters-large-screen{
  display:none;
}
.content-btn-filters {
  display: none;
}

.custom-filters-screen{
  
    // background-color: #6D8CA3;
    // box-shadow: 0 0 17px rgba(0, 0, 0, 0.5);
    background-color: rgba(32, 80, 114, 0.8);
    box-shadow: 1px 1px 4px #205072;
    padding: 23px;
    border-radius: 1rem;
    top: -1.8%;
    z-index: 10000000;
    position: absolute;
    right: 0px;
    min-height: 70%;
}
//////////////////////
.avatar-container {
  position: relative;
  display: inline-block;
}
/deep/.p-avatar img {
    width: 100%;
    height: 100%;
    border: 3px solid #fff;
    box-shadow: 0 0 5px rgba(86, 197, 150, 0.8);
}
.badge-profile {
    position: absolute;
    top: 50px;
    right: 6px;
    background-color: #56C596;
    color: white;
    border-radius: 50%;
    padding: 5px 5px;
    border: 2px solid  #fff;
}
.custom-margin{
  margin-left:60px;
}
.custom-padding{
  padding:1.5rem;
}
.custom-position{
  top:23%;
  left:0px;
}
.custom-overlay{
  top:0;
  position: absolute;
  width:100%;
  height: 100%;
  // background: rgba(32, 80, 114, 0.99); 
  background: var(--secondary-color); 
  opacity: 0.5;
  color:#fff;
  text-align: center;
  font-weight: bold;
}
.custom-number{
    position: absolute;
    left: 38%;
    bottom: 40%;
    font-weight: bold;
    color: #fff;
    font-size: large;
   text-shadow: 0px 2px 1px rgba(255, 255, 255, 0.5);

}
.custom-small{
  font-size: 10px; 
  font-style: italic;
}
.custom-gray{
  background-color: #F6F9F5;
  border-radius: 1.5rem;
  margin: 1rem 6rem;
  
}
.custom-icons{
  position: absolute;
  bottom:5%;
  right:2%;
}
/deep/.p-steps .p-steps-item .p-menuitem-link { 
  background:none
}
/deep/.p-steps .p-steps-item .p-menuitem-link:not(.p-disabled):focus {
  box-shadow: none !important; 
}

////////////triangle&span//////////////
.rating-text-span {
  right: 14px;
  bottom: -11px;
  font-size: smaller;
  color: white;
}

#triangle-right {
  position: relative;
  border-top: 22px solid transparent;
  border-left: 36px solid var(--secondary-color);
  border-bottom: 27px solid transparent;
  border-radius: 8px; 
}

.custom-height {
  height: fit-content;
}
.cover-pic{
  height:150px; 
  width: 100%;

}
.cover-pic img{
  width: 100%;
  height: 100%;
  border-radius: 1.5rem 0 0 0;
}

.custom-profile {
  position: absolute;
  top: 70%;
  left: 8%;
}

.custom-shadow {
  border-radius: 2rem;
  box-shadow: inset 0 0 10px rgba(86, 197, 150, 0.8);
  // box-shadow: inset 0 0 10px var(--shadow-success);
}
.custom-radius{
  border-radius: 0.37rem;
  text-align: center !important;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 9px;

}
.custom-border {
  border-left: 1px solid $primary;
}
.custom-cursor{
  cursor:pointer;
}
.custom-border-info {
  border-left: 1px solid $primary;
}
.change-content {
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #F1FAF7, #E0EBE8);
  border-radius: 1.5rem;
  box-shadow: 1px 1px 6px $primary;
  margin:0px;
}
.background-body{
  background: linear-gradient(180deg, #F1FAF7, #E0EBE8);
}
.custom-margin-info{
    margin: 0px 0.5rem ;
    
}
///////////////carousel//////////////////////////
.booking-item {
  height: 100%;
  border-radius: 2rem;
  box-shadow: inset 0 0 10px rgba(86, 197, 150, 0.8);
  margin: 0 0.3rem;
  padding: 1.5rem 0;
}
.booking-item-content {
  height: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
.bookings,.no-bookings{
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
}
// *************rtl******************
.rtl .custom-border {
  border-left:  0 !important;
  border-right:1px solid $primary;

}
.rtl .cover-pic img{
  width: 100%;
  height: 100%;
  border-radius: 0 1.5rem 0 0;
}
.rtl #triangle-right {
  position: relative;
  border-top: 22px solid transparent;
  border-left:0px;
  border-right: 35px solid var(--secondary-color);
  border-bottom: 24px solid transparent;
  border-radius: 8px; 
}
.rtl .rating-text-span {
  right:-30px;
  bottom: -10px;
  font-size: smaller;
  color: #fff;
}
.rtl .custom-icons{
  position: absolute;
  bottom:5%;
  left:2%;
  right:0%;
}
.rtl .custom-profile {
  position: absolute;
  top: 70%;
  right: 8%;
  left:0%;
}
.rtl .custom-margin{
    margin-left:0px;
    margin-right:60px;
}
.rtl .custom-position{
  top:23%;
  right:0px;
}
// *************media******************
@media only screen and (min-width: 1024px) and (max-width: 1439px) {
  .rtl .custom-border-info {
    border:0px; 
}
.custom-border-info {
    border-left:1px solid $primary;; 
}

}
@media only screen and (min-width: 1024px) and (max-width: 2560px) {
  .custom-gray{
    margin: 0;
    margin-top: 0.5rem ;
 }
 .custom-border {
  border-left: 1px solid $primary;
}
}
@media only screen and (min-width: 1440px){
  .rtl .custom-border-info {
    border:0px;
    border-right:1px solid $primary;
}
}
@media only screen and (min-width: 426px) and (max-width: 768px) {
  .custom-border {
    border-left: 0;
  }
  .cover-pic img {
    border-radius: 1.5rem 1.5rem 0 0 !important;
}
}
@media only screen and (min-width: 320px) and (max-width: 425px) {

.cover-pic img{
    width: 100%;
    height: 100%;
    border-radius: 1.5rem  1.5rem 0 0 !important;

}

.custom-border {
    border:0px;
}
.custom-border-info {
    border-left:0px;
}
.custom-border {
   border-left: 0;
}
.rtl .custom-border-info {
    border:0px;
    
}
  .rtl .custom-border {
    border:0px;
    
}
.custom-gray{
  margin: 0 ;
  margin-top: 0.5rem;

}

}
@media only screen and (min-width:320px)and (max-width:347px){
  .custom-margin-info{
    margin:0.5rem 0;
  } 
}
@media only screen and (min-width:320px)and (max-width:375px){
  .custom-gray{
    padding-left: 1.5rem;
}
}
@media only screen and (min-width:1440px)and (max-width:2560px){
.content-btn-filters {
  display: none;
}
.custom-filters-screen {
  display:none;
}
.custom-filters-large-screen{
  display:block;
}
  
}
@media only screen and (min-width:320px)and (max-width:1424px){
.content-btn-filters {
  display: block;
}
.custom-filters-large-screen{
  display:none;
}
.custom-filters-screen {
  display:block;
}
  
}

</style>
<!-- animate__fadeInDown -->