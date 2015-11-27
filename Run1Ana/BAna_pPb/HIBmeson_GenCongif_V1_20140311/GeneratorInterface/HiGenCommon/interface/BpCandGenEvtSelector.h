#ifndef _HI_BpCandGenEvtSelector_h__
#define _HI_BpCandGenEvtSelector_h__

#include "GeneratorInterface/HiGenCommon/interface/BaseHiGenEvtSelector.h"

class BpCandGenEvtSelector : public BaseHiGenEvtSelector {
 public:
   BpCandGenEvtSelector(const edm::ParameterSet&);
   virtual ~BpCandGenEvtSelector(){;}
   bool filter(HepMC::GenEvent *);

   double ptMin_;
   double etaMax_;
   int st_;
   int pdg_;
   int dau2pdg_;
   int dau2dau1pdg_;
   int dau2dau2pdg_;
   int nTrig_;

};

#endif
