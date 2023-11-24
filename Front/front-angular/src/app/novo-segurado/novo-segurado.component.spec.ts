import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovoSeguradoComponent } from './novo-segurado.component';

describe('NovoSeguradoComponent', () => {
  let component: NovoSeguradoComponent;
  let fixture: ComponentFixture<NovoSeguradoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NovoSeguradoComponent]
    });
    fixture = TestBed.createComponent(NovoSeguradoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
