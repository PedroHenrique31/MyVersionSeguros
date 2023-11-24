import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeguradoDetailComponent } from './segurado-detail.component';

describe('SeguradoDetailComponent', () => {
  let component: SeguradoDetailComponent;
  let fixture: ComponentFixture<SeguradoDetailComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SeguradoDetailComponent]
    });
    fixture = TestBed.createComponent(SeguradoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
