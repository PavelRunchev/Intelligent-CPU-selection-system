window.addEventListener('DOMContentLoaded', function () {
    const data = JSON.parse(document.getElementById('data-json').textContent);
    const user = JSON.parse(document.getElementById('user-data').textContent || '{}');

    const selectedBrand = user?.brand || "";
    const selectedModel = user?.model || "";
    const selectedCategory = user?.category || "";

    const brandSelect = document.getElementById('brandSelect');
    const modelSelect = document.getElementById('modelSelect');
    const categorySelect = document.getElementById('categorySelect');

    modelSelect.innerHTML = '<option value="">Избери модел</option>';
    categorySelect.innerHTML = '<option value="">Избери категория</option>';

    const brands = [... new Set(data.map(d => d.cpuName.split(" ")[0]))]
    let models = [...new Set(data.map(d => d.cpuName))];
    const categories = [...new Set(data.map(d => d.category))];

     brands.forEach(b => {
        const opt = document.createElement('option');
        opt.value = b;
        opt.textContent = b;
        brandSelect.appendChild(opt);
    });

    models.forEach(model => {
        const opt = document.createElement('option');
        opt.value = model;
        opt.textContent = model;
        modelSelect.appendChild(opt);
    });

     categories.forEach(category => {
         const opt = document.createElement('option');
         opt.value = category;
         opt.textContent = category;
         categorySelect.appendChild(opt);
     });


    brandSelect.addEventListener('change', function () {
        const selectedBrand = this.value;
        if (!selectedBrand || selectedBrand === 'Избери марка на процесора') return;

        modelSelect.innerHTML = '<option value="">Избери модел</option>';
        categorySelect.innerHTML = '<option value="">Избери категория</option>';

        const filteringModels = [...new Set(models.filter(m => m.split(" ")[0] === selectedBrand))];
        const filteringCategories = [...new Set(data.filter(b => b.brand === selectedBrand).map(b => b.category))];

        filteringModels.forEach(m => {
            const opt = document.createElement('option');
            opt.value = m;
            opt.textContent = m;
            modelSelect.appendChild(opt);
        });

        filteringCategories.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c;
            opt.textContent = c;
            categorySelect.appendChild(opt);
        });
    });

    modelSelect.addEventListener('change', function () {
        const selectedModel = this.value;
        if (!selectedModel) return;

        categorySelect.innerHTML = '<option value="">Избери категория</option>';

        const categories = [
            ...new Set(data.filter(d => d.cpuName === selectedModel).map(d => d.category))
        ];

        categories.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c;
            opt.textContent = c;
            categorySelect.appendChild(opt);
        });
    });



    if (selectedBrand && selectedBrand !== "") {
            brandSelect.value = selectedBrand;

            const models = [
                ...new Set(data.filter(d => d.brand === selectedBrand).map(d => d.cpuName))
            ];

            models.forEach(model => {
                const opt = document.createElement('option');
                opt.value = model;
                opt.textContent = model;

                if (model === selectedModel && opt.selected === false) opt.selected = true;

                modelSelect.appendChild(opt);
            });
    }

    if (selectedModel && selectedModel !== "") {
            const categories = [
                ...new Set(data.filter(d => d.cpuName === selectedModel).map(d => d.category))
            ];

            categories.forEach(c => {
                const opt = document.createElement('option');
                opt.value = c;
                opt.textContent = c;

                if (c === selectedCategory && opt.selected === false)
                    opt.selected = true;

                categorySelect.appendChild(opt);
            });
    }

    document.getElementById("resetBtn").addEventListener("click", function () {
        console.log("reset")
        const form = document.querySelector("form");
        console.log(form)
        form.reset();

        form.querySelectorAll("input").forEach(i => {
            console.log(i)
            i.value = ""
        });
    });
});


