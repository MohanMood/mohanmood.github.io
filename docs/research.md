# **Research Interest**

## **AI/ML for Molecular Property Prediction**

My research focuses on developing advanced AI/ML frameworks for predicting molecular and thermophysical properties of complex chemical systems, particularly ionic liquids (ILs), deep eutectic solvents (DESs), and organic compounds. By integrating quantum chemistry (COSMO-RS), molecular simulations, and machine learning, I enable accurate, scalable, and interpretable predictions across diverse chemical spaces. I have built models to predict key properties including viscosity, density, surface tension, speed of sound, polarity (Kamlet–Taft parameters), CO2 solubility, partition coefficients (logP), and enthalpy of vaporization. These models leverage physics-informed descriptors such as sigma profiles, as well as modern data-driven representations like chemprop, Mol2vec, and ChemBERTa embeddings. Using techniques such as CatBoost, neural networks (ANN/FFNN), graph neural networks, and deep learning, my models achieve high predictive accuracy (R2 ~ 0.95–0.99), significantly outperforming traditional regression and physics-only approaches. Additionally, I incorporate interpretability methods (e.g., SHAP) to uncover key molecular features governing property behavior. 

A major contribution of my work is enabling high-throughput virtual screening, where millions of candidate molecules can be evaluated computationally, drastically reducing reliance on costly and time-intensive experiments and computations. These AI/ML models have been applied to critical challenges in sustainable chemistry and energy, including carbon capture using DESs, lignocellulosic biomass processing, green solvent design, and advanced materials discovery. Furthermore, I explore NLP-based and generative AI approaches to design novel molecules with targeted properties, creating a pathway toward autonomous and data-driven chemical discovery. Overall, my research bridges physics-based modeling and artificial intelligence, providing a robust platform for accelerating innovation in green chemistry, biorefineries, and next-generation functional materials.


<div style="
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  align-items: start;
">
  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/ai-ml_workflow-gc-2025.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/ai-ml_workflow-gc-2025.gif" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/sigma-profile-features_ml-jctc-2024.jpeg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/sigma-profile-features_ml-jctc-2024.jpeg" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>


  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/chemical-space_os-nlp-mol2vec-2025.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/chemical-space_os-nlp-mol2vec-2025.png" alt="Chemical Space" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/activity-of-water-in-ils-gc-2025.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/activity-of-water-in-ils-gc-2025.gif" alt="Activity of ILs in water" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/shao-analysis-ils-viscosity-acs-2024.jpeg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/shao-analysis-ils-viscosity-acs-2024.jpeg" alt="SHAP analysis" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ai-ml/relationship-properties-gc-2025.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ai-ml/relationship-properties-gc-2025.gif" alt="Property relationships" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>
</div>


<h2 style="margin-bottom: 6px; margin-top: 16px;">Key Publications</h2>

<ol>
  <li>
    <div style="margin-bottom: 10px;">
      <b>Mohan M</b>*, Guggilam S, Bhowmik D, Kidder MK, Smith JC.
      Leveraging Natural Language Processing and Generative Models in Molecular Chemistry: Property Prediction and Novel Compound Generation.
      <i>ACS Sustainable Chem. Eng.</i>, (2025), 13, 48, 20737–20753.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acssuschemeng.5c08057" target="_blank" rel="noopener noreferrer">
        10.1021/acssuschemeng.5c08057
      </a>
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Kidder MK, Smith JC.
      Molecular Property Prediction for Very Large Databases with Natural Language Processing: A Case Study in Ionic Liquid Design.
      <i>Green Chemistry</i>, (2025), 27, 15106-15123.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2025/gc/d5gc02803e" target="_blank" rel="noopener noreferrer">
        10.1039/D5GC02803E
      </a>     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Gugulothu N, Guggilam S, Tatikonda T, Kidder MK, Smith JC.
      Physics-Informed Machine Learning to Predict Solvatochromic Parameters of Designer Solvents with Case Studies in CO2 and Lignin Dissolution.
      <i>Green Chemical Engineering</i>, (2025), 6(2), 275-287.
      DOI:
      <a href="https://www-sciencedirect-com.ornl.idm.oclc.org/science/article/pii/S2666952824000979" target="_blank" rel="noopener noreferrer">
        10.1016/j.cej.2024.156913
      </a>     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Jetti K, Smith MD, Demerdash O, Kidder MK, Smith JC*.
      Accurate Machine Learning for the Prediction of the Viscosities of Deep Eutectic Solvents.
      <i>Journal of Chemical Theory and Computation</i>, (2024), 20, 9, 3911–3926.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acs.jctc.3c01163" target="_blank" rel="noopener noreferrer">
        10.1021/acs.jctc.3c01163
      </a>      
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Demerdash O, Simmons BA, Smith JC, Kidder M, Singh S*.
      Accurate Prediction of Carbon Dioxide Capture by Deep Eutectic Solvents using Quantum Chemistry and a Neural Network.
      <i>Green Chemistry</i>, (2023), 25, 3475-3492.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2023/gc/d2gc04425k" target="_blank" rel="noopener noreferrer">
        10.1039/D2GC04425K
      </a>      
    </div>
  </li>
</ol>


## **Ionic Liquids & Deep Eutectic Solvents**

Ionic liquids (ILs) and deep eutectic solvents (DESs) are next-generation green solvents with tunable physicochemical properties for sustainable chemical processes. ILs are composed of organic cations and inorganic/organic anions, enabling precise control over solvation behavior, polarity, and reactivity. DESs, formed from hydrogen bond donors and acceptors, offer low-cost, biodegradable, and easily synthesizable alternatives to conventional solvents.

My research focuses on understanding how molecular structure governs solvent performance, particularly for biomass deconstruction, lignin dissolution, carbon capture, and plastic upcycling. Using molecular simulations and thermodynamic modeling, I identify key design principles such as hydrogen bonding strength, polarity matching, and solubility parameters. I demonstrate that anion chemistry plays a dominant role in disrupting biomass hydrogen-bond networks and enhancing dissolution.

Combined thermodynamics modelling, molecular dynamics, and machine learning approaches, I screen and design ILs and DESs for targeted applications. These solvents enable efficient fractionation of lignocellulosic biomass, improving accessibility to cellulose and hemicellulose for downstream conversion. My work also highlights bio-derived and low-toxicity solvent systems, advancing environmentally friendly alternatives for industrial processes. By integrating first-principles insights with predictive modeling, I develop scalable strategies for solvent discovery. ILs and DESs provide a powerful platform for designing sustainable, high-performance solvents for bioenergy, materials, and green chemistry applications.

<div style="
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  align-items: start;
">
  <div style="text-align: center;">
    <a href="/assets/research/ils-dess/ils-structure-1.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ils-dess/ils-structure-1.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ils-dess/ion-pair-ils.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ils-dess/ion-pair-ils.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ils-dess/Green-Chemistry_TOC_NewSampling.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ils-dess/Green-Chemistry_TOC_NewSampling.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/ils-dess/zncl2-des-curve.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/ils-dess/zncl2-des-curve.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

</div>


<h2 style="margin-bottom: 6px; margin-top: 16px;">Key Publications</h2>

<ol>
  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Kidder MK, Smith JC.
      Molecular Property Prediction for Very Large Databases with Natural Language Processing: A Case Study in Ionic Liquid Design.
      <i>Green Chemistry</i>, (2025), 27, 15106-15123.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2025/gc/d5gc02803e" target="_blank" rel="noopener noreferrer">
        10.1039/D5GC02803E
      </a>     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Gugulothu N, Guggilam S, Tatikonda T, Kidder MK, Smith JC.
      Physics-Informed Machine Learning to Predict Solvatochromic Parameters of Designer Solvents with Case Studies in CO2 and Lignin Dissolution.
      <i>Green Chemical Engineering</i>, (2025), 6(2), 275-287.
      DOI:
      <a href="https://www-sciencedirect-com.ornl.idm.oclc.org/science/article/pii/S2666952824000979" target="_blank" rel="noopener noreferrer">
        10.1016/j.cej.2024.156913
      </a>      
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Demerdash O, Simmons BA, Singh S, Kidder MK*, Smith JC*.
      Physics-Based Machine Learning Models Predict Carbon Dioxide Solubility in Chemically Reactive Deep Eutectic Solvents.
      <i>ACS Omega</i>, (2024), 9, 17, 19548–19559.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acsomega.4c01175" target="_blank" rel="noopener noreferrer">
        10.1021/acsomega.4c01175
      </a>     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      Verma R<sup>§</sup>, <b>Mohan M</b><sup>§</sup>, Banerjee T, Goud VV.
      Operational Strategies and Comprehensive Evaluation of Menthol Based Deep Eutectic Solvent for the Extraction of Lower Alcohols from Aqueous Media.
      <i>ACS Sustainable Chem. Eng.</i>, (2018), 6, 12, 16920-16932.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acssuschemeng.8b04255" target="_blank" rel="noopener noreferrer">
        10.1021/acssuschemeng.8b04255
      </a>
      <sup>§</sup> equal authorship      
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Naik PK, Banerjee T, Goud VV, Paul S.
      Solubility of Glucose in Tetrabutylammonium Bromide based Deep Eutectic Solvents: Experimental and Molecular Dynamic Simulations.
      <i>Fluid Phase Equilib.</i>, (2017); 448: 168-177.
      DOI:
      <a href="https://www.sciencedirect.com/science/article/abs/pii/S0378381217302212" target="_blank" rel="noopener noreferrer">
        10.1016/j.fluid.2017.05.024
      </a>     
    </div>
  </li>

</ol>


## **Biomass Pretreatment & Lignin Valorization**

My research focuses on developing sustainable and efficient strategies for lignocellulosic biomass deconstruction, enabling the production of biofuels, biochemicals, and advanced biomaterials. Lignocellulosic biomass, composed of cellulose, hemicellulose, and lignin, exhibits strong recalcitrance due to complex hydrogen bonding and cross-linked structures, making pretreatment a critical step. I have explored green solvent systems, including ionic liquids (ILs), protic ionic liquids (PILs), alkanolamines, subcritical water, and bio-derived solvents, to selectively disrupt biomass structure and enhance enzymatic accessibility. These solvents effectively reduce cellulose crystallinity, remove lignin, and improve sugar yields for downstream processing.

Using quantum chemistry, COSMO-RS modeling, and molecular dynamics simulations, my research provides molecular-level insights into solvent–lignin interactions, enabling predictive design of solvents tailored for efficient lignin solubilization and biomass fractionation. In addition, I have demonstrated the potential of dual-functional solvents (e.g., alkanolamines) that enable low-temperature, energy-efficient pretreatment while maintaining high sugar yields and facilitating downstream bioconversion. My work also explores novel green co-solvent systems (e.g., DMI/H₂O), revealing solvent-ratio-dependent mechanisms that enhance lignin dissolution and structural transformation at the molecular scale. Overall, this research integrates experiments, simulations, and process modeling to establish design principles for next-generation pretreatment technologies. These advances enable efficient lignin valorization and scalable, sustainable biorefineries for a circular bioeconomy.


<div style="
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  align-items: start;
">
  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/biomass-pretreatment_dmi-gc-2024.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/biomass-pretreatment_dmi-gc-2024.gif" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/consolidated-method-gc-2021.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/consolidated-method-gc-2021.gif" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/lignin-cellulose-hemi_icer-2018.jpeg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/lignin-cellulose-hemi_icer-2018.jpeg" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/rsm-cellulose-scw-rscadv-2015.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/rsm-cellulose-scw-rscadv-2015.gif" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/lignin-predictions-gc-2021.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/lignin-predictions-gc-2021.gif" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/biomass-pretreatment/biomass-pretreatment_scw-biores-2015.jpg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/biomass-pretreatment/biomass-pretreatment_scw-biores-2015.jpg" alt="Sigma profile featurization" style="width: 100%; max-width: 480px; border-radius: 8px;">
    </a>
  </div>

</div>


<h2 style="margin-bottom: 6px; margin-top: 16px;">Key Publications</h2>

<ol>
  <li>
    <div style="margin-bottom: 4px;">
      Huang K, Song J, Su K, Xu X, Jetti KD, Xu Y, Zhou X, Kidder MK, Smith JC, <b>Mohan M</b>*.
      Catalytic Conversion of Cellulose to Renewable Chemicals: A Review of 5-hydroxymethylfurfural, Levulinate Ester, and Sorbitol Production.
      <i>npj Sustainable materials</i>, (2026), 4, 7.
      DOI:
      <a href="https://www.nature.com/articles/s44296-025-00091-7" target="_blank" rel="noopener noreferrer">
        10.1038/s44296-025-00091-7
      </a>
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      Yang S<sup>§</sup>, <b>Mohan M</b><sup>§</sup>, Gao X, Yang X, Zhu J, Smith JC, Wang L.
      Multiscale Investigation of the Mechanism of Biomass Deconstruction in the Dimethyl isosorbide/Water Co-Solvent Pretreatment System.
      <i>Green Chemistry</i>, (2024), 26, 4758-4770.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2024/gc/d4gc00510d" target="_blank" rel="noopener noreferrer">
        10.1039/D4GC00510D
      </a>
      <sup>§</sup> equal authorship     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      Achinivu EC<sup>§</sup>, <b>Mohan M</b><sup>§</sup>, Choudhary H, Das L, Huang K, Magurudeniya HD, Pidatala VR, George A, Simmons BA, Gladden JM.
      A predictive tool-set for the identification of effective lignocellulosic pretreatment solvents: A case study of solvents tailored for lignin extraction.
      <i>Green Chemistry</i>, (2021), 23, 7269-7289.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2021/gc/d1gc01186c" target="_blank" rel="noopener noreferrer">
        10.1039/D1GC01186C
      </a>
      <sup>§</sup> equal authorship     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      Huang K, <b>Mohan M</b>, George A, Simmons BA, Yong X, Gladden JM.
      Integration of acetic acid catalysis with one-pot protic ionic liquid configuration to achieve high-efficient biorefinery of poplar biomass.
      <i>Green Chemistry</i>, (2021), 23, 6036-6049.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2021/gc/d1gc01727f" target="_blank" rel="noopener noreferrer">
        10.1039/D1GC01727F
      </a>       
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Deshavath NN, Banerjee T, Goud VV, Dasu VV.
      Ionic liquid and sulphuric acid based pretreatment of bamboo: biomass delignification and enzymatic hydrolysis for the production of reducing sugars.
      <i>Ind. Eng. Chem. Res.</i>, (2018), 57, 31, 10105-10117.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acs.iecr.8b00914" target="_blank" rel="noopener noreferrer">
        10.1021/acs.iecr.8b00914
      </a>     
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Timung R, Deshavath NN, Banerjee T, Goud VV, Dasu VV.
      Optimization and hydrolysis of cellulose under subcritical water treatment for the production of total reducing sugars.
      <i>RSC Advances</i>, (2015), 5: 103265-103275.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2015/ra/c5ra20319h" target="_blank" rel="noopener noreferrer">
        10.1039/C5RA20319H
      </a>        
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      Timung R, <b>Mohan M</b>, Chilukoti B, Sasmal S, Banerjee T, Goud VV.
      Optimization of dilute acid and hot water pretreatment of different lignocellulosic biomass: A comparative study.
      <i>Biomass Bioenergy</i>, (2015); 81: 9-18.
      DOI:
      <a href="https://www.sciencedirect.com/science/article/abs/pii/S096195341500183X" target="_blank" rel="noopener noreferrer">
        10.1016/j.biombioe.2015.05.006
      </a>        
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Banerjee T, Goud VV.
      Hydrolysis of bamboo biomass by subcritical water treatment.
      <i>Bioresour Technol.</i>, (2015), 191: 244-252.
      DOI:
      <a href="https://www.sciencedirect.com/science/article/abs/pii/S0960852415006744" target="_blank" rel="noopener noreferrer">
        10.1016/j.biortech.2015.05.010
      </a>        
    </div>
  </li>

</ol>

## **Molecular Simulation & First-Principles Modeling**

My research integrates first-principles calculations, molecular dynamics (MD), and multiscale simulations to uncover the fundamental mechanisms governing biomass deconstruction and solvent design. I employ advanced frameworks such as COSMO-RS, quantum chemical methods, and atomistic simulations to predict thermodynamic and molecular interactions in complex systems. Through large-scale screening of thousands of ionic liquids and solvents, my work identifies structure–property relationships that control lignin, cellulose, and hemicellulose solubility and reactivity. Using MD simulations, I quantify microscopic observables such as radial distribution functions, hydrogen-bond networks, radius of gyration, and solvent-accessible surface area to explain macroscopic behavior.

My work bridges molecular-scale insights with experimental validation, ensuring predictive accuracy in real-world biomass processing systems. I have developed multi-resolution modeling strategies to compute solubility parameters, interaction energies, and phase behavior of lignocellulosic systems. These approaches enable the rational discovery of sustainable solvents, including ionic liquids, deep eutectic solvents, and bio-derived solvents such as Cyrene. My research further extends to process-level insights, where simulations guide energy-efficient technologies such as nanocellulose fibrillation and biomass fractionation. By combining physics-based modeling with data-driven methods, my work accelerates the design of materials for green chemistry, bioenergy, and circular bioeconomy applications. Overall, this research establishes a predictive, multiscale framework for understanding and engineering complex molecular systems from first principles to industrial applications.

<div style="
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  align-items: start;
">
  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/ils-screening-lignin-scientific-2023.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/ils-screening-lignin-scientific-2023.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/lignin-dynamics-acs-sust-2022.jpeg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/lignin-dynamics-acs-sust-2022.jpeg" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/cosmo-rs-md-lifetime-lignin-gc-2021.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/cosmo-rs-md-lifetime-lignin-gc-2021.gif" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/sanky-lignin-ils-gc-2021.gif" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/sanky-lignin-ils-gc-2021.gif" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/lignin-il-md-gc-2021.png" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/lignin-il-md-gc-2021.png" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

  <div style="text-align: center;">
    <a href="/assets/research/Molecular-modelling/sdf-lignin-cyrene-acs-2022.jpeg" target="_blank" rel="noopener noreferrer">
      <img src="/assets/research/Molecular-modelling/sdf-lignin-cyrene-acs-2022.jpeg" alt="AI/ML workflow" style="width: 100%; max-width: 480px; border-radius: 8px;">
      </a>
  </div>

</div>


<h2 style="margin-bottom: 6px; margin-top: 16px;">Key Publications</h2>

<ol>
  <li>
    <div style="margin-bottom: 4px;">
      Rukmani SJ, Yu Y, <b>Mohan M</b>, Sethuraman V, Goswami M, Smith JC.
      Coarse-Grained Molecular Dynamics Simulation of Solvent-Dependent Cellulose Nanofiber Interactions.
      <i>Biophysical Journal</i>, (2026), 125(2), 3827-3852.
      DOI:
      <a href="https://www-sciencedirect-com.ornl.idm.oclc.org/science/article/pii/S0006349525005338" target="_blank" rel="noopener noreferrer">
        10.1016/j.bpj.2025.08.021
      </a>
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Simmons BA*, Sale K, Singh S.
      Multiscale Molecular Simulations for the Solvation of Lignin in Ionic Liquids.
      <i>Scientific Reports</i>, (2023), 13, 271.
      DOI:
      <a href="https://www.nature.com/articles/s41598-022-25372-2" target="_blank" rel="noopener noreferrer">
        10.1038/s41598-022-25372-2
      </a>      
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>*, Sale K, Kalb R, Simmons BA, Gladden JM, Singh S.
      Multiscale Molecular Simulations Strategies for Understanding the Delignification Mechanism of Biomass in Cyrene.
      <i>ACS Sustainable Chem. Eng.</i>, (2022), 10, 33, 11016–11029.
      DOI:
      <a href="https://pubs.acs.org/doi/10.1021/acssuschemeng.2c03373" target="_blank" rel="noopener noreferrer">
        10.1021/acssuschemeng.2c03373
      </a>       
    </div>
  </li> 

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Huang K, Pidatala VR, Simmons BA, Singh S, Sale K, Gladden JM.
      Prediction of Solubility Parameters of Lignin and Ionic Liquids Using Multi-resolution Simulation Approaches.
      <i>Green Chemistry</i>, (2022), 24, 1165-1176.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2022/gc/d1gc03798f" target="_blank" rel="noopener noreferrer">
        10.1039/D1GC03798F
      </a>    
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Choudhary H, George A, Simmons BA, Sale K, Gladden JM.
      Towards Understanding of Delignification of Grassy and Woody Biomass in Cholinium-based Ionic Liquids.
      <i>Green Chemistry</i>, (2021), 23, 6020-6035.
      DOI:
      <a href="https://pubs.rsc.org/en/content/articlelanding/2021/gc/d1gc01622a" target="_blank" rel="noopener noreferrer">
        10.1039/D1GC01622A
      </a>       
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Viswanath P, Banerjee T, Goud VV.
      Multiscale Modeling Strategies and Experimental Insights for the Solvation of Cellulose and Hemicellulose in Ionic Liquids.
      <i>Mol. Phys.</i>, (2018); 116: 2108-2128.
      DOI:
      <a href="https://www.tandfonline.com/doi/full/10.1080/00268976.2018.1447152" target="_blank" rel="noopener noreferrer">
        10.1080/00268976.2018.1447152
      </a>      
    </div>
  </li>

  <li>
    <div style="margin-bottom: 4px;">
      <b>Mohan M</b>, Banerjee T, Goud VV.
      Effect of Protic and Aprotic Solvents on the Mechanism of Cellulose Dissolution in Ionic Liquids: A Combined Molecular Dynamics and Experimental Insight.
      <i>ChemistrySelect</i>, (2016); 1(15): 4823–4832.
      DOI:
      <a href="https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/slct.201601094" target="_blank" rel="noopener noreferrer">
        10.1002/slct.201601094
      </a>         
    </div>
  </li>

</ol>