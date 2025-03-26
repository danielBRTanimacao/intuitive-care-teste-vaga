<template>
    <div
        class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-green-300 to-blue-500 p-4"
    >
        <h1 class="text-3xl font-bold text-center text-white mb-8">
            Detalhes das Administradoras
        </h1>
        <div v-if="loading" class="text-center text-white text-lg">
            Carregando...
        </div>
        <div v-else-if="error" class="text-center text-red-500 text-lg">
            Erro ao carregar os dados!
        </div>
        <div v-else class="w-full max-w-4xl">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div
                    v-for="(item, index) in paginatedData"
                    :key="index"
                    class="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg p-6 rounded-xl shadow-lg"
                >
                    <h2 class="text-xl font-semibold text-gray-800 mb-4">
                        {{ item.Razao_Social }}
                    </h2>
                    <ul class="space-y-2">
                        <li>
                            <span class="font-medium text-gray-600">CNPJ:</span>
                            <span class="text-gray-800">{{ item.CNPJ }}</span>
                        </li>
                        <li>
                            <span class="font-medium text-gray-600"
                                >Registro ANS:</span
                            >
                            <span class="text-gray-800">{{
                                item.Registro_ANS
                            }}</span>
                        </li>
                        <li>
                            <span class="font-medium text-gray-600"
                                >Endereço:</span
                            >
                            <span class="text-gray-800"
                                >{{ item.Logradouro }}, {{ item.Numero }} -
                                {{ item.Bairro }}</span
                            >
                        </li>
                        <li>
                            <span class="font-medium text-gray-600"
                                >Cidade/UF:</span
                            >
                            <span class="text-gray-800"
                                >{{ item.Cidade }}/{{ item.UF }}</span
                            >
                        </li>
                        <li>
                            <span class="font-medium text-gray-600">CEP:</span>
                            <span class="text-gray-800">{{ item.CEP }}</span>
                        </li>
                        <li>
                            <span class="font-medium text-gray-600"
                                >Telefone:</span
                            >
                            <span class="text-gray-800">{{
                                item.Telefone
                            }}</span>
                        </li>
                        <li>
                            <span class="font-medium text-gray-600"
                                >Representante:</span
                            >
                            <span class="text-gray-800">{{
                                item.Representante
                            }}</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="mt-6 flex items-center justify-center space-x-4">
                <button
                    @click="prevPage"
                    :disabled="currentPage === 1"
                    class="px-4 py-2 bg-white text-gray-800 rounded hover:bg-gray-200 disabled:opacity-50"
                >
                    Anterior
                </button>
                <span class="text-white">
                    Página {{ currentPage }} de {{ totalPages }}
                </span>
                <button
                    @click="nextPage"
                    :disabled="currentPage === totalPages"
                    class="px-4 py-2 bg-white text-gray-800 rounded hover:bg-gray-200 disabled:opacity-50"
                >
                    Próxima
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";

const jsonData = ref([]);
const loading = ref(true);
const error = ref(false);

const itemsPerPage = 4;
const currentPage = ref(1);

const totalPages = computed(() => {
    return Math.ceil(jsonData.value.length / itemsPerPage);
});

const paginatedData = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    return jsonData.value.slice(start, start + itemsPerPage);
});

function nextPage() {
    if (currentPage.value < totalPages.value) {
        currentPage.value++;
    }
}

function prevPage() {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
}

onMounted(async () => {
    try {
        const response = await axios.get("http://127.0.0.1:5000/api");
        jsonData.value = response.data;
    } catch (err) {
        console.error("Erro ao buscar dados:", err);
        error.value = true;
    } finally {
        loading.value = false;
    }
});
</script>
