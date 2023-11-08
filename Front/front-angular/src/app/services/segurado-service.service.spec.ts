import { TestBed } from '@angular/core/testing';

import { SeguradoServiceService } from './segurado-service.service';

describe('SeguradoServiceService', () => {
  let service: SeguradoServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SeguradoServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
