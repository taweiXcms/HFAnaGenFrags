#include <iostream>
#include "GeneratorInterface/HiGenCommon/interface/BpCandGenEvtSelector.h" // made by Hyunchul

BpCandGenEvtSelector::BpCandGenEvtSelector(const edm::ParameterSet& iConfig)
   : BaseHiGenEvtSelector(iConfig)
{
   ptMin_ = iConfig.getParameter<double>("ptMin");
   etaMax_ = iConfig.getParameter<double>("etaMax");
   pdg_ = iConfig.getParameter<int>("pdg");
   dau2pdg_ = iConfig.getParameter<int>("dau2pdg");
   dau2dau1pdg_ = iConfig.getParameter<int>("dau2dau1pdg");
   dau2dau2pdg_ = iConfig.getParameter<int>("dau2dau2pdg");
   st_ = iConfig.getParameter<int>("status");
   nTrig_ = iConfig.getParameter<int>("minimumCandidates");
}

bool BpCandGenEvtSelector::filter(HepMC::GenEvent *evt) {
	std::cout << "start of filter" << std::endl;
    int found = 0;
    HepMC::GenEvent::particle_const_iterator begin = evt->particles_begin();
    HepMC::GenEvent::particle_const_iterator end = evt->particles_end();
    for(HepMC::GenEvent::particle_const_iterator it = begin; it != end; ++it) {
	//std::cout << "--- pdgId: " << (*it)->pdg_id();
	//std::cout << ", status : " << (*it)->status() << std::endl;
    	if (abs((*it)->pdg_id()) == pdg_ && (*it)->momentum().perp()>ptMin_ && fabs((*it)->momentum().eta())<etaMax_) {
		bool hasJp=false, hasKp=false;
		std::cout << "We have B+ candidate, pt : " << (*it)->momentum().perp() << " , eta : " << (*it)->momentum().eta() << std::endl;   
			for( HepMC::GenVertex::particle_iterator aDaughter=(*it)->end_vertex()->particles_begin(HepMC::descendants) ; aDaughter!=(*it)->end_vertex()->particles_end(HepMC::descendants);aDaughter++) {
				if ((*aDaughter)->pdg_id()==22) continue;
				//Jpsi
//				if ((*aDaughter)->pdg_id()==443 && (*aDaughter)->momentum().perp()>ptMin_ && fabs((*aDaughter)->momentum().eta())<etaMax_) {
//                if ((*aDaughter)->pdg_id()==443 && (*aDaughter)->momentum().perp()>ptMin_ && fabs((*aDaughter)->momentum().eta())<etaMax_ && (*aDaughter)->end_vertex()) {                                  
                if ((*aDaughter)->pdg_id()==443 && (*aDaughter)->end_vertex()) {                                  
					std::cout << "*** Daughter : J/Psi, pt : " << (*aDaughter)->momentum().perp() << " , eta : " << (*aDaughter)->momentum().eta() << std::endl;   
					bool hasidp13=false, hasidm13=false;
					for (HepMC::GenVertex::particle_iterator byaDaughter=(*aDaughter)->end_vertex()->particles_begin(HepMC::descendants); byaDaughter != (*aDaughter)->end_vertex()->particles_end(HepMC::descendants);byaDaughter++) {
						if ((*byaDaughter)->pdg_id()==22) continue;
//						if ((*byaDaughter)->pdg_id()==13 && (*byaDaughter)->momentum().perp()>ptMin_ && fabs((*byaDaughter)->momentum().eta())<etaMax_) hasidp13=true;
//						if ((*byaDaughter)->pdg_id()==-13 && (*byaDaughter)->momentum().perp()>ptMin_ && fabs((*byaDaughter)->momentum().eta())<etaMax_) hasidm13=true;
						if ((*byaDaughter)->pdg_id()==13 ) hasidp13=true;
						if ((*byaDaughter)->pdg_id()==-13 ) hasidm13=true;
					}
					if (hasidp13==true && hasidm13==true) hasJp=true;
				}
				//Kstar, Ks, Phi, K+
//				if (abs((*aDaughter)->pdg_id())==dau2pdg_ && (*aDaughter)->status()==1 && (*aDaughter)->momentum().perp()>ptMin_ && fabs((*aDaughter)->momentum().eta())<etaMax_) {
//				if (abs((*aDaughter)->pdg_id())==dau2pdg_ && (*aDaughter)->momentum().perp()>ptMin_ && fabs((*aDaughter)->momentum().eta())<etaMax_) {
				if (abs((*aDaughter)->pdg_id())==dau2pdg_) {
					std::cout << "*** Daughter : "<<(*aDaughter)->pdg_id()<<", pt : " << (*aDaughter)->momentum().perp() << " , eta : " << (*aDaughter)->momentum().eta() << std::endl;   
					bool hasdaudau1=false, hasdaudau2=false;
					if ( dau2dau1pdg_ == 0 && dau2dau2pdg_ == 0 && (*aDaughter)->status()==1) {hasdaudau1=true; hasdaudau2=true;}//No dau2 dau needed
					//if ( dau2dau1pdg_ == 0 && dau2dau2pdg_ == 0 ) {hasdaudau1=true; hasdaudau2=true;}//No dau2 dau needed
					else if((*aDaughter)->end_vertex()){
						//std::cout<<"test debug"<<std::endl;
						for (HepMC::GenVertex::particle_iterator byaDaughter=(*aDaughter)->end_vertex()->particles_begin(HepMC::descendants); byaDaughter != (*aDaughter)->end_vertex()->particles_end(HepMC::descendants);byaDaughter++) {
							if ((*byaDaughter)->pdg_id()==22) continue;
//							if (abs((*byaDaughter)->pdg_id())==dau2dau1pdg_ && (*byaDaughter)->status()==1 && (*byaDaughter)->momentum().perp()>ptMin_ && fabs((*byaDaughter)->momentum().eta())<etaMax_) hasdaudau1=true;
//							if (abs((*byaDaughter)->pdg_id())==dau2dau2pdg_ && (*byaDaughter)->status()==1 && (*byaDaughter)->momentum().perp()>ptMin_ && fabs((*byaDaughter)->momentum().eta())<etaMax_) hasdaudau2=true;
							if (abs((*byaDaughter)->pdg_id())==dau2dau1pdg_ && (*byaDaughter)->status()==1 ) hasdaudau1=true;
							if (abs((*byaDaughter)->pdg_id())==dau2dau2pdg_ && (*byaDaughter)->status()==1 ) hasdaudau2=true;
						}
					}
					if (hasdaudau1==true && hasdaudau2==true) hasKp=true;
				} 
			}
			if (hasJp==true && hasKp==true) {found++;std::cout << "### We have " << found << " signal in ths event ###" << std::endl;}
//			if (hasJp==true) {found++;std::cout << "### We have " << found << " signal in ths event ###" << std::endl;}
		}
		// if (found == nTrig_) return true;
	}
	if (found >= nTrig_) return true; else return false;
	//return true;
}

