document.addEventListener("DOMContentLoaded", () => {
    // ==========================================
    // 1. SCROLL REVEAL ANIMATIONS
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, { root: null, threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    revealElements.forEach(el => revealObserver.observe(el));

    // ==========================================
    // 2. BLASTING SIMULATOR LOGIC (DTC-02)
    // ==========================================
    const triggerBtn = document.getElementById('triggerBlastBtn');
    const btnCarregar = document.getElementById('btnCarregar');
    const btnCancelar = document.getElementById('btnCancelar');
    
    const detonators = document.querySelectorAll('.detonator-node');
    const telemetryLog = document.getElementById('telemetryLog');
    const simStatus = document.getElementById('simStatus');
    const statusLights = document.getElementById('statusLights');
    const rockStructure = document.querySelector('.rock-structure');
    const fracturePath = document.getElementById('fracturePath');
    
    let isBlasting = false;
    let isCharged = false;

    function addTelemetryLog(msg, type = 'system') {
        const div = document.createElement('div');
        div.className = `log-entry ${type}`;
        div.innerText = msg;
        telemetryLog.appendChild(div);
        telemetryLog.scrollTop = telemetryLog.scrollHeight;
    }

    function createDustParticle(x, y) {
        const particle = document.createElement('div');
        particle.className = 'dust-particle active';
        const size = Math.random() * 4 + 2; 
        const offsetX = (Math.random() - 0.5) * 40;
        
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `calc(${x} + ${offsetX}px)`;
        particle.style.top = y;
        
        rockStructure.appendChild(particle);
        setTimeout(() => { particle.remove(); }, 2000);
    }
    
    function resetSimulatorState() {
        simStatus.innerText = "SISTEMA DESARMADO";
        simStatus.style.color = "var(--color-silver-dim)";
        isBlasting = false;
        isCharged = false;
        triggerBtn.disabled = true;
        btnCarregar.disabled = false;
        if (statusLights) {
            const lights = statusLights.querySelectorAll('.light');
            lights.forEach(light => light.classList.remove('on'));
        }
        
        detonators.forEach(d => d.classList.remove('firing'));
        fracturePath.style.stroke = "rgba(255,255,255,0.1)";
        fracturePath.style.strokeDasharray = "10, 5";
    }

    btnCarregar.addEventListener('click', () => {
        if (isBlasting || isCharged) return;
        isCharged = true;
        simStatus.innerText = "SISTEMA CARREGADO";
        simStatus.style.color = "var(--color-lightning)";
        if (statusLights) {
            const lights = statusLights.querySelectorAll('.light');
            lights.forEach((light, i) => {
                setTimeout(() => {
                    light.classList.add('on');
                }, i * 250);
            });
        }
        triggerBtn.disabled = false;
        btnCarregar.disabled = true;
        addTelemetryLog("> Tensão nos capacitores nominal. Pronto para disparo.", "system");
    });
    
    btnCancelar.addEventListener('click', () => {
        if (isBlasting) return; // Cannot cancel mid-sequence
        if (isCharged) {
            addTelemetryLog("> Disparo abortado. Descarregando...", "system");
        }
        resetSimulatorState();
    });

    triggerBtn.addEventListener('click', () => {
        if (isBlasting || !isCharged) return;
        isBlasting = true;
        isCharged = false;
        
        simStatus.innerText = "SEQUÊNCIA INICIADA";
        simStatus.style.color = "#ef4444";
        if (statusLights) {
            const lights = statusLights.querySelectorAll('.light');
            lights.forEach(light => light.classList.remove('on'));
        }
        triggerBtn.disabled = true;
        btnCancelar.disabled = true;
        
        telemetryLog.innerHTML = "";
        addTelemetryLog("> Iniciando protocolo de desmonte em série...", "system");
        
        const sortedDetonators = Array.from(detonators).sort((a, b) => 
            parseInt(a.getAttribute('data-delay')) - parseInt(b.getAttribute('data-delay'))
        );

        let maxDelay = 0;

        sortedDetonators.forEach((detonator, index) => {
            const delay = parseInt(detonator.getAttribute('data-delay'));
            if (delay > maxDelay) maxDelay = delay;

            setTimeout(() => {
                detonator.classList.add('firing');
                const formattedDelay = delay.toString().padStart(3, '0');
                addTelemetryLog(`[+${formattedDelay}ms] NÓ #${(index+1).toString().padStart(2,'0')}: DETONADO (SUCESSO)`, "fire");
                
                for(let i=0; i<8; i++) {
                    createDustParticle(detonator.style.left, detonator.style.top);
                }

                if (index === sortedDetonators.length - 1) {
                    fracturePath.style.transition = "all 0.5s ease-out";
                    fracturePath.style.stroke = "var(--color-lightning)";
                    fracturePath.style.strokeDasharray = "0";
                    setTimeout(() => {
                        fracturePath.style.stroke = "rgba(255,255,255,0.1)";
                        fracturePath.style.strokeDasharray = "10, 5";
                    }, 1500);
                }
            }, delay);
        });

        setTimeout(() => {
            addTelemetryLog("> Sequência concluída. Integridade: 100%.", "system");
            btnCancelar.disabled = false; // re-enable abort button just as reset
            setTimeout(resetSimulatorState, 2000);
        }, maxDelay + 1000);
    });

    // ==========================================
    // 3. CONTACT FORM LOGIC (CRM SIMULATION)
    // ==========================================
    const form = document.getElementById("leadForm");
    const msgDiv = document.getElementById("formMsg");
    const submitBtn = document.getElementById("submitBtn");
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = submitBtn.querySelector('.spinner');

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        
        // Coleta de dados
        const leadData = {
            nome: document.getElementById("nome").value,
            empresa: document.getElementById("empresa").value,
            whatsapp: document.getElementById("whatsapp").value,
            email: document.getElementById("email").value,
            segmento: document.getElementById("segmento").value,
            origem: "Landing Page Explochip V2 Premium",
            timestamp: new Date().toISOString()
        };

        console.log("🔥 NOVO LEAD ALTO TICKET - DNA NETWORK:", leadData);

        // UI State: Loading
        btnText.style.display = 'none';
        loader.style.display = 'inline-block';
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.7';

        setTimeout(() => {
            // UI State: Success
            msgDiv.style.color = "var(--color-lightning)";
            msgDiv.innerHTML = "✅ Solicitação enviada. A engenharia da Explochip entrará em contato em breve.";
            form.reset();
            
            // Restore Button
            btnText.style.display = 'block';
            loader.style.display = 'none';
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            
            // Clear message
            setTimeout(() => { msgDiv.innerHTML = ""; }, 6000);
        }, 1500);
    });
});
