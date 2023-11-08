import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeguradoComponent } from './segurado.component';

describe('SeguradoComponent', () => {
  let component: SeguradoComponent;
  let fixture: ComponentFixture<SeguradoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SeguradoComponent]
    });
    fixture = TestBed.createComponent(SeguradoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
